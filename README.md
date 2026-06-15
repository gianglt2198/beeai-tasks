# search-agent

A progressive series of hands-on exercises exploring the [BeeAI Framework](https://github.com/i-am-bee/beeai-framework) for building LLM-powered agents in Python. Tasks go from raw prompt templates up to multi-agent systems with tool-use and human-in-the-loop controls.

## Stack

- **[BeeAI Framework](https://github.com/i-am-bee/beeai-framework)** — agent orchestration, tools, memory, middleware
- **LangChain + OpenRouter** — LLM backend (defaults to `deepseek/deepseek-v4-flash`)
- **Pydantic** — structured output validation
- **Python 3.11+**, Poetry

## Setup

```bash
poetry install
cp .env.example .env  # add OPENAI_API_KEY and optionally OPENAI_API_BASE / OPENAI_CHAT_MODEL
```

The shared LLM is configured in [llm.py](llm.py). It wraps a LangChain `ChatOpenAI` client inside BeeAI's `LangChainChatModel`.

## Tasks

| File | Concept |
|------|---------|
| [task_3.py](task_3.py) | **Prompt templates** — manual `{{variable}}` substitution, evaluates ML project proposals |
| [task_4.py](task_4.py) | **Structured output** — Pydantic `response_format`, generates a typed `BusinessPlan` |
| [task_5.py](task_5.py) | **Basic `RequirementAgent`** — pure LLM, no tools, cybersecurity analysis |
| [task_6.py](task_6.py) | **Tool use** — adds `WikipediaTool` (max 2 calls) for research-grounded answers |
| [task_7.py](task_7.py) | **Reasoning + research** — combines `ThinkTool` and `WikipediaTool` |
| [task_8.py](task_8.py) | **Strict `ConditionalRequirement`** — declarative ordering: Think first, Wikipedia only after Think |
| [task_9.py](task_9.py) | **ReAct pattern** — `force_after=Tool` enforces Think → Act → Think → Act cycles |
| [task_10.py](task_10.py) | **Human-in-the-loop** — `AskPermissionRequirement` gates Wikipedia calls on user approval |
| [task_11.py](task_11.py) | **Custom tool** — `SimpleCalculatorTool` with Pydantic input schema and safe `eval` |
| [task_12.py](task_12.py) | **Multi-agent system** — Travel Coordinator delegates to three specialist agents (Destination, Weather, Language/Culture) via `HandoffTool` |

Run any task directly:

```bash
poetry run python task_12.py
```

## Key BeeAI concepts covered

- `RequirementAgent` with `ConditionalRequirement` for declarative tool-call constraints (`force_at_step`, `only_after`, `min/max_invocations`, `consecutive_allowed`)
- `AskPermissionRequirement` for human-in-the-loop tool gating
- `GlobalTrajectoryMiddleware` for execution tracing
- `HandoffTool` for routing between specialized sub-agents
- `UnconstrainedMemory` for full conversation history within an agent run
- Custom `Tool` subclasses with typed Pydantic input schemas
