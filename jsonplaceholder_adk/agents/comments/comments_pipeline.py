from google.adk.agents import LlmAgent, SequentialAgent

from .schemas.comments import CommentsOutput
from .tools.jsonplaceholder_comments import get_comments
from .instructions.comments import FETCH_COMMENTS_INSTRUCTION, FORMAT_COMMENTS_INSTRUCTION

fetch_comments_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_comments_agent",
    description="Fetches comments from JSONPlaceholder.",
    instruction=FETCH_COMMENTS_INSTRUCTION,
    tools=[get_comments],
    # tools=[get_users, ...],
    output_key="raw_comments_json",
)

format_comments_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_comments_agent",
    description="Formats comments data into strict JSON.",
    instruction=FORMAT_COMMENTS_INSTRUCTION,
    output_schema=CommentsOutput,
    output_key="formatted_comments_json",
)

comments_pipeline_agent = SequentialAgent(
    name="comments_pipeline_agent",
    sub_agents=[fetch_comments_agent, format_comments_agent],
)
