from google.adk.agents import LlmAgent, SequentialAgent

from .schemas.users import SingleUserOutput
from .tools.jsonplaceholder_users import get_user
from .instructions.users import FETCH_USER_INSTRUCTION, FORMAT_USER_INSTRUCTION

fetch_user_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="fetch_user_agent",
    description="Fetches a user from JSONPlaceholder by id.",
    instruction=FETCH_USER_INSTRUCTION,
    tools=[get_user],
    output_key="raw_user_json",
)

format_user_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="format_user_agent",
    description="Formats a user into strict JSON.",
    instruction=FORMAT_USER_INSTRUCTION,
    output_schema=SingleUserOutput,
    output_key="formatted_user_json",
)

user_pipeline_agent = SequentialAgent(
    name="user_pipeline_agent",
    sub_agents=[fetch_user_agent, format_user_agent],
)
