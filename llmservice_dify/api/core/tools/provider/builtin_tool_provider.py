from abc import abstractmethod
from os import listdir, path
from typing import Any

from core.helper.module_import_helper import load_single_subclass_from_source
from core.tools.entities.tool_entities import ToolParameter, ToolProviderCredentials, ToolProviderType
from core.tools.entities.values import ToolLabelEnum, default_tool_label_dict
from core.tools.errors import (
    ToolNotFoundError,
    ToolParameterValidationError,
    ToolProviderNotFoundError,
)
from core.tools.provider.tool_provider import ToolProviderController
from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.tool.tool import Tool
from core.tools.utils.yaml_utils import load_yaml_file


class BuiltinToolProviderController(ToolProviderController):
    def __init__(self, **data: Any) -> None:
        if self.provider_type in {ToolProviderType.API, ToolProviderType.APP}:
            super().__init__(**data)
            return

        # load provider yaml
        provider = self.__class__.__module__.split(".")[-1]
        yaml_path = path.join(path.dirname(path.realpath(__file__)), "builtin", provider, f"{provider}.yaml")
        try:
            provider_yaml = load_yaml_file(yaml_path, ignore_error=False)
        except Exception as e:
            raise ToolProviderNotFoundError(f"can not load provider yaml for {provider}: {e}")

        if "credentials_for_provider" in provider_yaml and provider_yaml["credentials_for_provider"] is not None:
            # set credentials name
            for credential_name in provider_yaml["credentials_for_provider"]:
                provider_yaml["credentials_for_provider"][credential_name]["name"] = credential_name

        super().__init__(
            **{
                "identity": provider_yaml["identity"],
                "credentials_schema": provider_yaml.get("credentials_for_provider", None),
            }
        )

    def _get_builtin_tools(self) -> list[Tool]:
        """
        returns a list of tools that the provider can provide

        :return: list of tools
        """
        if self.tools:
            return self.tools

        provider = self.identity.name
        tool_path = path.join(path.dirname(path.realpath(__file__)), "builtin", provider, "tools")
        # get all the yaml files in the tool path
        tool_files = list(filter(lambda x: x.endswith(".yaml") and not x.startswith("__"), listdir(tool_path)))
        tools = []
        for tool_file in tool_files:
            # get tool name
            tool_name = tool_file.split(".")[0]
            tool = load_yaml_file(path.join(tool_path, tool_file), ignore_error=False)

            # get tool class, import the module
            assistant_tool_class = load_single_subclass_from_source(
                module_name=f"core.tools.provider.builtin.{provider}.tools.{tool_name}",
                script_path=path.join(
                    path.dirname(path.realpath(__file__)), "builtin", provider, "tools", f"{tool_name}.py"
                ),
                parent_type=BuiltinTool,
            )
            tool["identity"]["provider"] = provider
            tools.append(assistant_tool_class(**tool))

        self.tools = tools
        return tools

    def get_credentials_schema(self) -> dict[str, ToolProviderCredentials]:
        """
        returns the credentials schema of the provider

        :return: the credentials schema
        """
        if not self.credentials_schema:
            return {}

        return self.credentials_schema.copy()

    def get_tools(self) -> list[Tool]:
        """
        returns a list of tools that the provider can provide

        :return: list of tools
        """
        return self._get_builtin_tools()

    def get_tool(self, tool_name: str) -> Tool:
        """
        returns the tool that the provider can provide
        """
        return next(filter(lambda x: x.identity.name == tool_name, self.get_tools()), None)

    def get_parameters(self, tool_name: str) -> list[ToolParameter]:
        """
        returns the parameters of the tool

        :param tool_name: the name of the tool, defined in `get_tools`
        :return: list of parameters
        """
        tool = next(filter(lambda x: x.identity.name == tool_name, self.get_tools()), None)
        if tool is None:
            raise ToolNotFoundError(f"tool {tool_name} not found")
        return tool.parameters

    @property
    def need_credentials(self) -> bool:
        """
        returns whether the provider needs credentials

        :return: whether the provider needs credentials
        """
        return self.credentials_schema is not None and len(self.credentials_schema) != 0

    @property
    def provider_type(self) -> ToolProviderType:
        """
        returns the type of the provider

        :return: type of the provider
        """
        return ToolProviderType.BUILT_IN

    @property
    def tool_labels(self) -> list[str]:
        """
        returns the labels of the provider

        :return: labels of the provider
        """
        label_enums = self._get_tool_labels()
        return [default_tool_label_dict[label].name for label in label_enums]

    def _get_tool_labels(self) -> list[ToolLabelEnum]:
        """
        returns the labels of the provider
        """
        return self.identity.tags or []

    def validate_parameters(self, tool_id: int, tool_name: str, tool_parameters: dict[str, Any]) -> None:
        """
        validate the parameters of the tool and set the default value if needed

        :param tool_name: the name of the tool, defined in `get_tools`
        :param tool_parameters: the parameters of the tool
        """
        tool_parameters_schema = self.get_parameters(tool_name)

        tool_parameters_need_to_validate: dict[str, ToolParameter] = {}
        for parameter in tool_parameters_schema:
            tool_parameters_need_to_validate[parameter.name] = parameter

        for parameter in tool_parameters:
            if parameter not in tool_parameters_need_to_validate:
                raise ToolParameterValidationError(f"parameter {parameter} not found in tool {tool_name}")

            # check type
            parameter_schema = tool_parameters_need_to_validate[parameter]
            if parameter_schema.type == ToolParameter.ToolParameterType.STRING:
                if not isinstance(tool_parameters[parameter], str):
                    raise ToolParameterValidationError(f"parameter {parameter} should be string")

            elif parameter_schema.type == ToolParameter.ToolParameterType.NUMBER:
                if not isinstance(tool_parameters[parameter], int | float):
                    raise ToolParameterValidationError(f"parameter {parameter} should be number")

                if parameter_schema.min is not None and tool_parameters[parameter] < parameter_schema.min:
                    raise ToolParameterValidationError(
                        f"parameter {parameter} should be greater than {parameter_schema.min}"
                    )

                if parameter_schema.max is not None and tool_parameters[parameter] > parameter_schema.max:
                    raise ToolParameterValidationError(
                        f"parameter {parameter} should be less than {parameter_schema.max}"
                    )

            elif parameter_schema.type == ToolParameter.ToolParameterType.BOOLEAN:
                if not isinstance(tool_parameters[parameter], bool):
                    raise ToolParameterValidationError(f"parameter {parameter} should be boolean")

            elif parameter_schema.type == ToolParameter.ToolParameterType.SELECT:
                if not isinstance(tool_parameters[parameter], str):
                    raise ToolParameterValidationError(f"parameter {parameter} should be string")

                options = parameter_schema.options
                if not isinstance(options, list):
                    raise ToolParameterValidationError(f"parameter {parameter} options should be list")

                if tool_parameters[parameter] not in [x.value for x in options]:
                    raise ToolParameterValidationError(f"parameter {parameter} should be one of {options}")

            tool_parameters_need_to_validate.pop(parameter)

        for parameter in tool_parameters_need_to_validate:
            parameter_schema = tool_parameters_need_to_validate[parameter]
            if parameter_schema.required:
                raise ToolParameterValidationError(f"parameter {parameter} is required")

            # the parameter is not set currently, set the default value if needed
            if parameter_schema.default is not None:
                default_value = parameter_schema.type.cast_value(parameter_schema.default)
                tool_parameters[parameter] = default_value

    def validate_credentials(self, credentials: dict[str, Any]) -> None:
        """
        validate the credentials of the provider

        :param tool_name: the name of the tool, defined in `get_tools`
        :param credentials: the credentials of the tool
        """
        # validate credentials format
        self.validate_credentials_format(credentials)

        # validate credentials
        self._validate_credentials(credentials)

    @abstractmethod
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        """
        validate the credentials of the provider

        :param tool_name: the name of the tool, defined in `get_tools`
        :param credentials: the credentials of the tool
        """
        pass
