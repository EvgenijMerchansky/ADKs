from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool

from ..agents.users.users_pipeline import users_pipeline_agent
from ..agents.users.user_pipeline import user_pipeline_agent
from ..agents.posts.post_pipeline import post_pipeline_agent
from ..agents.posts.posts_pipeline import posts_pipeline_agent

from ..callbacks.formatting import pretty_pipeline_result

from ..prompts.root import ROOT_AGENT_INSTRUCTION

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