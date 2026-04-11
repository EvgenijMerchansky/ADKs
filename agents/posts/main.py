import os
import logging

from a2a.types import AgentCard
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from posts.agent import root_agent

PORT = int(os.environ.get("PORT", 8000))
POSTS_AGENT_URL = os.environ.get("POSTS_AGENT_URL", "http://posts-agent:8000")

agent_card = AgentCard(
    name="posts_agent",
    url=POSTS_AGENT_URL,
    description="Agent that works with posts operations.",
    version="1.0.0",
    capabilities={},
    skills=[],
    defaultInputModes=["application/json"],
    defaultOutputModes=["text/plain"],
    supportsExtendedAgentCard=False,
)

a2a_app = to_a2a(root_agent, port=PORT, agent_card=agent_card)

if __name__ == "__main__":
    import uvicorn

    logger = logging.getLogger(__name__)
    logger.info(f"Starting Posts Agent on port {PORT}")
    uvicorn.run(a2a_app, host="0.0.0.0", port=PORT)
