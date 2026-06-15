import asyncio 
import logging
import os 

from typing import List
from pydantic import BaseModel, Field

from beeai_framework.backend import UserMessage, SystemMessage

from llm import get_llm

class BusinessPlan(BaseModel):
    """A comprehensive business plan structure"""
    business_name: str = Field(description="Catchy name for the business")
    elevator_pitch: str = Field(description="30-second description of the business")
    target_market: str = Field(description="Primary target audience")
    unique_value_proposition: str = Field(description="What makes this business special")
    revenue_streams: List[str] = Field(description="Ways the business will make money")
    startup_costs: str = Field(description="Estimated initial investment needed")
    key_success_factors: List[str] = Field(description="Critical elements for success")

async def structured_output_example():
    llm = get_llm()

    messages = [
        SystemMessage(content="You are an expert business consultant and entrepreneur."),
        UserMessage(content="Create a business plan for a mobile app that helps people find and book unique local experiences in their city.")
    ]

    response = await llm.run(
        messages,
        response_format=BusinessPlan,
    )

    print("User: Create a business plan for a mobile app that helps people find and book unique local experiences in their city.")
    print("\nAI-Generated Business Plan:")
    print(f"Business Name: {response.output_structured.business_name}")
    print(f"Elevator Pitch: {response.output_structured.elevator_pitch}")
    print(f"Target Market: {response.output_structured.target_market}")
    print(f"Unique Value Proposition: {response.output_structured.unique_value_proposition}")
    print(f"Revenue Streams: {', '.join(response.output_structured.revenue_streams)}")
    print(f"Startup Costs: {response.output_structured.startup_costs}")
    print(f"Key Success Factors:")
    for factor in response.output_structured.key_success_factors:
        print(f"  - {factor}")

async def main():
    logging.getLogger("asyncio").setLevel(logging.CRITICAL)
    await structured_output_example()

if __name__ == "__main__":
    asyncio.run(main())

