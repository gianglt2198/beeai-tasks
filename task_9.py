
import asyncio
import logging

from llm import get_llm

from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.agents.requirement.requirements.conditional import ConditionalRequirement
from beeai_framework.memory import UnconstrainedMemory
from beeai_framework.tools.search.wikipedia import WikipediaTool
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool
from beeai_framework.tools.think import ThinkTool

SYSTEM_INSTRUCTIONS = """You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures"""

ANALYSIS_QUERY = """Analyze the cybersecurity risks of quantum computing for financial institutions.
    What are the main threats, timeline for concern, and recommended preparation strategies?"""


async def wikipedia_enhanced_agent_example():
    """ReAct pattern: Think -> Tool -> Think -> Tool -> ... -> Answer."""
    llm = get_llm()

    wikipedia_agent = RequirementAgent(
        llm=llm,
        tools=[ThinkTool(), WikipediaTool()],
        memory=UnconstrainedMemory(),
        middlewares=[GlobalTrajectoryMiddleware(included=[Tool])],
        requirements=[
            ConditionalRequirement(
                ThinkTool,                 
                force_at_step=1,
                force_after=Tool,
                min_invocations=1,
                max_invocations=5,
                consecutive_allowed=False
            ),
            # ConditionalRequirement(
            #     WikipediaTool,
            #     only_after=[ThinkTool],
            #     min_invocations=1,
            #     max_invocations=2
            # ),
        ]
    )

    result = await wikipedia_agent.run(ANALYSIS_QUERY)
    print(f"\nReAct Analysis:\n{result.output_structured.response}")


async def main() -> None:
    logging.getLogger('asyncio').setLevel(logging.CRITICAL)
    await wikipedia_enhanced_agent_example()


if __name__ == "__main__":
    asyncio.run(main())
