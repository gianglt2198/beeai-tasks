import asyncio
import logging 

from llm import get_llm

from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.memory import UnconstrainedMemory

SYSTEM_INSTRUCTIONS = """
You are an expert cybersecurity analyst specializing in threat assessment and risk analysis.

Your methodology:
1. Analyze the threat landscape systematically
2. Research authoritative sources when available
3. Provide comprehensive risk assessment with actionable recommendations
4. Focus on practical, implementable security measures
"""

ANALYSIS_QUERY = """Analyz the cybersecurity risks of quantum computing for financial institutions.
    What are the main threats, timeline for concern, and recommended preparation strategies?"""

async def minimal_tracked_agent_example():
    llm = get_llm()

    minimal_agent = RequirementAgent(
        llm=llm,
        tools=[],
        memory=UnconstrainedMemory(),
        instructions=SYSTEM_INSTRUCTIONS
    )

    result = await minimal_agent.run(ANALYSIS_QUERY)

    print(f"\nPure LLM Analysis:\n{result.output_structured.response}")


async def main() -> None:
    logging.getLogger('asyncio').setLevel(logging.CRITICAL)
    await minimal_tracked_agent_example()


if __name__ == "__main__":
    asyncio.run(main())