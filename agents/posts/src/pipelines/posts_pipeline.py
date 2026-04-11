from google.adk.agents import LlmAgent, SequentialAgent

from google.genai import types

from posts.src.tools.posts_service import get_post, get_posts
from posts.src.tools.formatters import prettify_json
from posts.src.instructions import FETCH_POSTS_INSTRUCTION, FORMAT_POSTS_INSTRUCTION

AGENT_CONFIG = types.GenerateContentConfig(temperature=0.3, top_p=0.9, top_k=40)

fetch_posts_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_posts_agent",
    description="Fetches post/posts.",
    instruction=FETCH_POSTS_INSTRUCTION,
    tools=[get_post, get_posts],
    output_key="raw_posts_json",
    generate_content_config=AGENT_CONFIG
)

format_posts_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_posts_agent",
    description="Formats post/posts data into strict JSON.",
    instruction=FORMAT_POSTS_INSTRUCTION,
    tools=[prettify_json],
    output_key="formatted_posts_json",
    generate_content_config=AGENT_CONFIG
)

posts_pipeline_agent = SequentialAgent(
    name="posts_pipeline_agent",
    sub_agents=[fetch_posts_agent, format_posts_agent],
)
