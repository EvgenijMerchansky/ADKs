from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from .users.users_pipeline import users_pipeline_agent
from .users.user_pipeline import user_pipeline_agent
from .posts.post_pipeline import post_pipeline_agent
from .posts.posts_pipeline import posts_pipeline_agent

from jsonplaceholder_adk.shared.callbacks.formatting import pretty_pipeline_result

ROOT_AGENT_INSTRUCTION = """
Ти дружній асистент.
Якщо користувач просто вітається — відповідай звичайним текстом.
Якщо користувач просить отримати користувача/користувачів із JSONPlaceholder — використовуй users pipelines.
Якщо користувач просить отримати публыкацію/публыкації із JSONPlaceholder — використовуй posts pipelines.
Якщо користувач просить отримати публыкацію/публыкації певного юзера із JSONPlaceholder — використовуй posts pipelines.
Усі відповіді повинні повертатися - відформатовані в JSON форматі.
"""

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="JSONPlaceholder root agent.",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[
        AgentTool(
            agent=users_pipeline_agent,
            skip_summarization=False,
        ),
        AgentTool(
            agent=user_pipeline_agent,
            skip_summarization=False,
        ),
        AgentTool(
            agent=post_pipeline_agent,
            skip_summarization=False,
        ),
        AgentTool(
            agent=posts_pipeline_agent,
            skip_summarization=False,
        ),
    ],
    after_tool_callback=pretty_pipeline_result,
)
