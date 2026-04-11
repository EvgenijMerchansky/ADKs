from google.adk.agents import LlmAgent, SequentialAgent

from google.genai import types

from users.src.tools.users_service import get_user, get_users
from users.src.tools.formatters import prettify_json
from users.src.instructions import FETCH_USERS_INSTRUCTION, FORMAT_USERS_INSTRUCTION

AGENT_CONFIG = types.GenerateContentConfig(temperature=0.3, top_p=0.9, top_k=40)

fetch_users_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_users_agent",
    description="Fetches user/users.",
    instruction=FETCH_USERS_INSTRUCTION,
    tools=[get_user, get_users],
    output_key="raw_users_json",
    generate_content_config=AGENT_CONFIG
)

format_users_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_users_agent",
    description="Formats user/users data into strict JSON.",
    instruction=FORMAT_USERS_INSTRUCTION,
    tools=[prettify_json],
    output_key="formatted_users_json",
    generate_content_config=AGENT_CONFIG
)

users_pipeline_agent = SequentialAgent(
    name="users_pipeline_agent",
    sub_agents=[fetch_users_agent, format_users_agent],
)
