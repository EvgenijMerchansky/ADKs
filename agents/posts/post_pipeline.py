from google.adk.agents import LlmAgent, SequentialAgent

from ...schemas.posts import SinglePostOutput
from ...tools.jsonplaceholder_posts import get_post
from ...prompts.posts import FETCH_POST_INSTRUCTION, FORMAT_POST_INSTRUCTION

fetch_post_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_post_agent",
    description="Fetches a post from JSONPlaceholder by id.",
    instruction=FETCH_POST_INSTRUCTION,
    tools=[get_post],
    output_key="raw_post_json",
)

format_post_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_post_agent",
    description="Formats a post into strict JSON.",
    instruction=FORMAT_POST_INSTRUCTION,
    output_schema=SinglePostOutput,
    output_key="formatted_post_json",
)

post_pipeline_agent = SequentialAgent(
    name="post_pipeline_agent",
    sub_agents=[fetch_post_agent, format_post_agent],
)