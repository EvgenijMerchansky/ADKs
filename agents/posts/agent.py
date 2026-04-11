import logging

from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool

from google.genai import types

from a2a.types import AgentCard

from posts.src.pipelines.posts_pipeline import posts_pipeline_agent

from posts.src.instructions import POSTS_AGENT_INSTRUCTION

AGENT_CONFIG = types.GenerateContentConfig(temperature=0.4, top_p=0.9, top_k=40)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="posts_agent",
    description="Handles only posts fetching and users selection tasks. Never handles users or comments..",
    instruction=POSTS_AGENT_INSTRUCTION,
    tools=[
        AgentTool(
            agent=posts_pipeline_agent,
            skip_summarization=False,
        )
    ],
    generate_content_config=AGENT_CONFIG
)

logger = logging.getLogger(__name__)
logger.info(f"Posts Agent '{root_agent.name}' initialized successfully")
