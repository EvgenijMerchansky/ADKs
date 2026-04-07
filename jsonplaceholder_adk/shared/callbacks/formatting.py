import json
from typing import Any, Dict, Optional

from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext

supported_tools = {
    "users_pipeline_agent",
    "user_pipeline_agent",
    "posts_pipeline_agent",
    "post_pipeline_agent",
}

service_keys = {
    "formatted_users_json",
    "formatted_user_json",
    "raw_users_json",
    "raw_user_json",
    "raw_posts_json",
    "raw_post_json",
}


def pretty_pipeline_result(
        tool: BaseTool,
        args: Dict[str, Any],
        tool_context: ToolContext,
        tool_response: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    if tool.name not in supported_tools:
        return None

    value = tool_response.get("result", tool_response)

    if isinstance(value, dict) and len(value) == 1:
        only_key = next(iter(value.keys()))
        if only_key in service_keys:
            value = value[only_key]

    pretty = json.dumps(value, indent=2, ensure_ascii=False)
    return {"result": pretty}
