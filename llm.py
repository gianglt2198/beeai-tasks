import os
import asyncio
import sys
import traceback

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from beeai_framework.adapters.langchain.backend.chat import LangChainChatModel

load_dotenv()

langchain_llm = ChatOpenAI(
    model=os.getenv("OPENAI_CHAT_MODEL", "deepseek/deepseek-v4-flash"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1"),
    temperature=0,
)


def get_llm() -> LangChainChatModel:
    return LangChainChatModel(langchain_llm, allow_parallel_tool_calls=True)
