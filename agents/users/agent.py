import logging

from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool

from google.genai import types

from a2a.types import AgentCard

from users.src.pipelines.users_pipeline import users_pipeline_agent

from users.src.instructions import USERS_AGENT_INSTRUCTION

AGENT_CONFIG = types.GenerateContentConfig(temperature=0.4, top_p=0.9, top_k=40)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="users_agent",
    description="Handles only users fetching and user selection tasks. Never handles posts or comments..",
    instruction=USERS_AGENT_INSTRUCTION,
    tools=[
        AgentTool(
            agent=users_pipeline_agent,
            skip_summarization=False,
        )
    ],
    generate_content_config=AGENT_CONFIG
)

logger = logging.getLogger(__name__)
logger.info(f"Uses Agent '{root_agent.name}' initialized successfully")
