import logging

from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool

from google.genai import types

from a2a.types import AgentCard

from comments.src.pipelines.comments_pipeline import comments_pipeline_agent

from comments.src.instructions import COMMENTS_AGENT_INSTRUCTION

AGENT_CONFIG = types.GenerateContentConfig(temperature=0.4, top_p=0.9, top_k=40)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="comments_agent",
    description="Handles only comments fetching and comments selection tasks. Never handles users or posts..",
    instruction=COMMENTS_AGENT_INSTRUCTION,
    tools=[
        AgentTool(
            agent=comments_pipeline_agent,
            skip_summarization=False,
        )
    ],
    generate_content_config=AGENT_CONFIG
)

logger = logging.getLogger(__name__)
logger.info(f"Comments Agent '{root_agent.name}' initialized successfully")
