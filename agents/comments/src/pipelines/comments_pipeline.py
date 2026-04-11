from google.adk.agents import LlmAgent, SequentialAgent

from google.genai import types

from comments.src.tools.comments_service import get_comment, get_comments
from comments.src.tools.formatters import prettify_json
from comments.src.instructions import FETCH_COMMENTS_INSTRUCTION, FORMAT_COMMENTS_INSTRUCTION

AGENT_CONFIG = types.GenerateContentConfig(temperature=0.3, top_p=0.9, top_k=40)

fetch_comments_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_comments_agent",
    description="Fetches comment/comments.",
    instruction=FETCH_COMMENTS_INSTRUCTION,
    tools=[get_comment, get_comments],
    output_key="raw_comments_json",
    generate_content_config=AGENT_CONFIG
)

format_comments_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_comments_agent",
    description="Formats comment/comments data into strict JSON.",
    instruction=FORMAT_COMMENTS_INSTRUCTION,
    tools=[prettify_json],
    output_key="formatted_comments_json",
    generate_content_config=AGENT_CONFIG
)

comments_pipeline_agent = SequentialAgent(
    name="comments_pipeline_agent",
    sub_agents=[fetch_comments_agent, format_comments_agent],
)
