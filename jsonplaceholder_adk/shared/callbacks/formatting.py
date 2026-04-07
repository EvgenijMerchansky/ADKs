import json
from typing import Any, Dict, Optional

from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext

from jsonplaceholder_adk.shared.constants.pipelines import available_pipelines
from jsonplaceholder_adk.shared.constants.formatting import formatting_keys


def pretty_pipeline_result(
        tool: BaseTool,
        args: Dict[str, Any],
        tool_context: ToolContext,
        tool_response: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    if tool.name not in available_pipelines:
        return None

    value = tool_response.get("result", tool_response)

    if isinstance(value, dict) and len(value) == 1:
        only_key = next(iter(value.keys()))
        if only_key in formatting_keys:
            value = value[only_key]

    pretty = json.dumps(value, indent=2, ensure_ascii=False)
    return {"result": pretty}
