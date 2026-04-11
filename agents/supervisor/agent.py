import os
import logging

from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool

from google.genai import types

from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

from a2a.types import AgentCard, AgentSkill

from supervisor.src.instructions import SUPERVISOR_AGENT_INSTRUCTION, SUPERVISOR_AGENT_DESCRIPTION

SUPERVISOR_AGENT_URL = os.environ.get("SUPERVISOR_AGENT_URL", "http://localhost:8000")

AGENT_CONFIG = types.GenerateContentConfig(temperature=0.7, top_p=0.9, top_k=40)

supervisor_agent_card = AgentCard(
    name="supervisor_agent",
    url=SUPERVISOR_AGENT_URL,
    description=SUPERVISOR_AGENT_DESCRIPTION,
    version="1.0.0",
    capabilities={
        "streaming": True,
        "pushNotifications": False,
        "stateTransitionHistory": True
    },
    skills=[
        AgentSkill(
            id="users_returning",
            name="Users returning",
            description="Returns single user or users list or user info from users_agent",
            tags=["users"],
            examples=["Get all users", "Get users list", "Get single user", "Get user", "Get user data",
                      "Get user info", "Get user by user_id"]
        ),
        AgentSkill(
            id="posts_returning",
            name="posts returning",
            description="Returns single post or posts list or post info from posts_agent",
            tags=["posts"],
            examples=["Get all posts", "Get posts list", "Get single post", "Get post", "Get post data",
                      "Get post info", "Get post by post_id"]
        ),
        AgentSkill(
            id="comments_returning",
            name="comments returning",
            description="Returns single comment or comments list or post info from comments_agent",
            tags=["comments"],
            examples=["Get all comments", "Get comments list", "Get single comment", "Get comment", "Get comment data",
                      "Get comment info", "Get comment by comment_id"]
        )
    ],
    defaultInputModes=["application/json", "text/plain"],
    defaultOutputModes=["application/json", "text/plain"],
    supportsAuthenticatedExtendedCard=False,
)

SUPERVISOR_USE_LOCAL_AGENTS = os.environ.get("SUPERVISOR_USE_LOCAL_AGENTS", "false").lower() == "true"

if SUPERVISOR_USE_LOCAL_AGENTS:
    from users.agent import root_agent as users_agent
    from posts.agent import root_agent as posts_agent
    from comments.agent import root_agent as comments_agent

    root_agent = Agent(
        model="gemini-2.5-flash",
        name="supervisor_agent",
        description=SUPERVISOR_AGENT_DESCRIPTION,
        instruction=SUPERVISOR_AGENT_INSTRUCTION,
        tools=[
            AgentTool(agent=users_agent),
            AgentTool(agent=posts_agent),
            AgentTool(agent=comments_agent)
        ],
        generate_content_config=AGENT_CONFIG
    )

else:
    from google.adk.a2a.utils.agent_to_a2a import to_a2a

    USERS_AGENT_URL = os.environ.get("USERS_AGENT_URL", "http://users-agent:8000")
    POSTS_AGENT_URL = os.environ.get("POSTS_AGENT_URL", "http://posts-agent:8000")
    COMMENTS_AGENT_URL = os.environ.get("COMMENTS_AGENT_URL", "http://comments-agent:8000")

    users_agent = RemoteA2aAgent(
        name="users_agent",
        description="Agent that works with users operations.",
        agent_card=f"{USERS_AGENT_URL}/.well-known/agent-card.json",
        use_legacy=False,
    )

    posts_agent = RemoteA2aAgent(
        name="posts_agent",
        description="Agent that works with posts operations.",
        agent_card=f"{POSTS_AGENT_URL}/.well-known/agent-card.json",
        use_legacy=False,
    )

    comments_agent = RemoteA2aAgent(
        name="comments_agent",
        description="Agent that works with comments operations.",
        agent_card=f"{COMMENTS_AGENT_URL}/.well-known/agent-card.json",
        use_legacy=False,
    )

    root_agent = Agent(
        model="gemini-2.5-flash",
        name="supervisor_agent",
        description=SUPERVISOR_AGENT_DESCRIPTION,
        instruction=SUPERVISOR_AGENT_INSTRUCTION,
        sub_agents=[users_agent, posts_agent, comments_agent],
        generate_content_config=AGENT_CONFIG
    )

    a2a_app = to_a2a(root_agent, port=8000, agent_card=supervisor_agent_card)

logger = logging.getLogger(__name__)
logger.info(f"Supervisor Agent '{root_agent.name}' initialized successfully")
