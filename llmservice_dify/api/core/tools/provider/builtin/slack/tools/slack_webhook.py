from typing import Any, Union

import httpx

from core.tools.entities.tool_entities import ToolInvokeMessage
from core.tools.tool.builtin_tool import BuiltinTool


class SlackWebhookTool(BuiltinTool):
    def _invoke(
        self, user_id: str, tool_parameters: dict[str, Any]
    ) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        """
        Incoming Webhooks
        API Document: https://api.slack.com/messaging/webhooks
        """

        content = tool_parameters.get("content", "")
        if not content:
            return self.create_text_message("Invalid parameter content")

        webhook_url = tool_parameters.get("webhook_url", "")

        if not webhook_url.startswith("https://hooks.slack.com/"):
            return self.create_text_message(
                f"Invalid parameter webhook_url ${webhook_url}, not a valid Slack webhook URL"
            )

        headers = {
            "Content-Type": "application/json",
        }
        params = {}
        payload = {
            "text": content,
        }

        try:
            res = httpx.post(webhook_url, headers=headers, params=params, json=payload)
            if res.is_success:
                return self.create_text_message("Text message was sent successfully")
            else:
                return self.create_text_message(
                    f"Failed to send the text message, status code: {res.status_code}, response: {res.text}"
                )
        except Exception as e:
            return self.create_text_message("Failed to send message through webhook. {}".format(e))
