from google.adk.agents import LlmAgent, SequentialAgent

from .schemas.comments import SingleCommentOutput
from .tools.jsonplaceholder_comments import get_comment
from .instructions.comments import FETCH_COMMENT_INSTRUCTION, FORMAT_COMMENT_INSTRUCTION

fetch_comment_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_comment_agent",
    description="Fetches a comment from JSONPlaceholder by id.",
    instruction=FETCH_COMMENT_INSTRUCTION,
    tools=[get_comment],
    output_key="raw_comment_json",
)

format_comment_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_comment_agent",
    description="Formats a comment into strict JSON.",
    instruction=FORMAT_COMMENT_INSTRUCTION,
    output_schema=SingleCommentOutput,
    output_key="formatted_comment_json",
)

comment_pipeline_agent = SequentialAgent(
    name="comment_pipeline_agent",
    sub_agents=[fetch_comment_agent, format_comment_agent],
)
