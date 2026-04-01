from google.adk.agents import LlmAgent, SequentialAgent

from ...schemas.posts import PostsOutput
from ...tools.jsonplaceholder_posts import get_posts
from ...prompts.posts import FETCH_POSTS_INSTRUCTION, FORMAT_POSTS_INSTRUCTION

fetch_posts_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_posts_agent",
    description="Fetches posts from JSONPlaceholder.",
    instruction=FETCH_POSTS_INSTRUCTION,
    tools=[get_posts],
    # tools=[get_users, ...],
    output_key="raw_posts_json",
)

format_posts_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_posts_agent",
    description="Formats posts data into strict JSON.",
    instruction=FORMAT_POSTS_INSTRUCTION,
    output_schema=PostsOutput,
    output_key="formatted_posts_json",
)

posts_pipeline_agent = SequentialAgent(
    name="posts_pipeline_agent",
    sub_agents=[fetch_posts_agent, format_posts_agent],
)