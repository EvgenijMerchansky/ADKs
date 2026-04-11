import os
import logging

from a2a.types import AgentCard
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from comments.agent import root_agent

PORT = int(os.environ.get("PORT", 8000))
COMMENTS_AGENT_URL = os.environ.get("COMMENTS_AGENT_URL", "http://comments-agent:8000")

agent_card = AgentCard(
    name="comments_agent",
    url=COMMENTS_AGENT_URL,
    description="Agent that works with comments operations.",
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
    logger.info(f"Starting Comments Agent on port {PORT}")
    uvicorn.run(a2a_app, host="0.0.0.0", port=PORT)
