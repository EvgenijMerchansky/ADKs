from google.adk.agents import LlmAgent, SequentialAgent

from .schemas.users import UsersOutput
from .tools.jsonplaceholder_users import get_users
from .instructions.users import FETCH_USERS_INSTRUCTION, FORMAT_USERS_INSTRUCTION

fetch_users_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_users_agent",
    description="Fetches users from JSONPlaceholder.",
    instruction=FETCH_USERS_INSTRUCTION,
    tools=[get_users],
    # tools=[get_users, ...],
    output_key="raw_users_json",
)

format_users_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_users_agent",
    description="Formats users data into strict JSON.",
    instruction=FORMAT_USERS_INSTRUCTION,
    output_schema=UsersOutput,
    output_key="formatted_users_json",
)

users_pipeline_agent = SequentialAgent(
    name="users_pipeline_agent",
    sub_agents=[fetch_users_agent, format_users_agent],
)
