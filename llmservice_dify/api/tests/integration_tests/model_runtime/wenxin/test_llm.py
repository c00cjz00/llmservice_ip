import os
from collections.abc import Generator
from time import sleep

import pytest

from core.model_runtime.entities.llm_entities import LLMResult, LLMResultChunk, LLMResultChunkDelta
from core.model_runtime.entities.message_entities import AssistantPromptMessage, SystemPromptMessage, UserPromptMessage
from core.model_runtime.entities.model_entities import AIModelEntity
from core.model_runtime.errors.validate import CredentialsValidateFailedError
from core.model_runtime.model_providers.wenxin.llm.llm import ErnieBotLargeLanguageModel


def test_predefined_models():
    model = ErnieBotLargeLanguageModel()
    model_schemas = model.predefined_models()
    assert len(model_schemas) >= 1
    assert isinstance(model_schemas[0], AIModelEntity)


def test_validate_credentials_for_chat_model():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    with pytest.raises(CredentialsValidateFailedError):
        model.validate_credentials(
            model="ernie-bot", credentials={"api_key": "invalid_key", "secret_key": "invalid_key"}
        )

    model.validate_credentials(
        model="ernie-bot",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
    )


def test_invoke_model_ernie_bot():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.invoke(
        model="ernie-bot",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[UserPromptMessage(content="Hello World!")],
        model_parameters={
            "temperature": 0.7,
            "top_p": 1.0,
        },
        stop=["you"],
        user="abc-123",
        stream=False,
    )

    assert isinstance(response, LLMResult)
    assert len(response.message.content) > 0
    assert response.usage.total_tokens > 0


def test_invoke_model_ernie_bot_turbo():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.invoke(
        model="ernie-bot-turbo",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[UserPromptMessage(content="Hello World!")],
        model_parameters={
            "temperature": 0.7,
            "top_p": 1.0,
        },
        stop=["you"],
        user="abc-123",
        stream=False,
    )

    assert isinstance(response, LLMResult)
    assert len(response.message.content) > 0
    assert response.usage.total_tokens > 0


def test_invoke_model_ernie_8k():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.invoke(
        model="ernie-bot-8k",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[UserPromptMessage(content="Hello World!")],
        model_parameters={
            "temperature": 0.7,
            "top_p": 1.0,
        },
        stop=["you"],
        user="abc-123",
        stream=False,
    )

    assert isinstance(response, LLMResult)
    assert len(response.message.content) > 0
    assert response.usage.total_tokens > 0


def test_invoke_model_ernie_bot_4():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.invoke(
        model="ernie-bot-4",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[UserPromptMessage(content="Hello World!")],
        model_parameters={
            "temperature": 0.7,
            "top_p": 1.0,
        },
        stop=["you"],
        user="abc-123",
        stream=False,
    )

    assert isinstance(response, LLMResult)
    assert len(response.message.content) > 0
    assert response.usage.total_tokens > 0


def test_invoke_stream_model():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.invoke(
        model="ernie-3.5-8k",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[UserPromptMessage(content="Hello World!")],
        model_parameters={
            "temperature": 0.7,
            "top_p": 1.0,
        },
        stop=["you"],
        stream=True,
        user="abc-123",
    )

    assert isinstance(response, Generator)
    for chunk in response:
        assert isinstance(chunk, LLMResultChunk)
        assert isinstance(chunk.delta, LLMResultChunkDelta)
        assert isinstance(chunk.delta.message, AssistantPromptMessage)
        assert len(chunk.delta.message.content) > 0 if chunk.delta.finish_reason is None else True


def test_invoke_model_with_system():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.invoke(
        model="ernie-bot",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[SystemPromptMessage(content="你是Kasumi"), UserPromptMessage(content="你是谁？")],
        model_parameters={
            "temperature": 0.7,
            "top_p": 1.0,
        },
        stop=["you"],
        stream=False,
        user="abc-123",
    )

    assert isinstance(response, LLMResult)
    assert "kasumi" in response.message.content.lower()


def test_invoke_with_search():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.invoke(
        model="ernie-bot",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[UserPromptMessage(content="北京今天的天气怎么样")],
        model_parameters={
            "temperature": 0.7,
            "top_p": 1.0,
            "disable_search": True,
        },
        stop=[],
        stream=True,
        user="abc-123",
    )

    assert isinstance(response, Generator)
    total_message = ""
    for chunk in response:
        assert isinstance(chunk, LLMResultChunk)
        assert isinstance(chunk.delta, LLMResultChunkDelta)
        assert isinstance(chunk.delta.message, AssistantPromptMessage)
        total_message += chunk.delta.message.content
        print(chunk.delta.message.content)
        assert len(chunk.delta.message.content) > 0 if not chunk.delta.finish_reason else True

    # there should be 对不起、我不能、不支持……
    assert "不" in total_message or "抱歉" in total_message or "无法" in total_message


def test_get_num_tokens():
    sleep(3)
    model = ErnieBotLargeLanguageModel()

    response = model.get_num_tokens(
        model="ernie-bot",
        credentials={"api_key": os.environ.get("WENXIN_API_KEY"), "secret_key": os.environ.get("WENXIN_SECRET_KEY")},
        prompt_messages=[UserPromptMessage(content="Hello World!")],
        tools=[],
    )

    assert isinstance(response, int)
    assert response == 10
