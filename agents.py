import os
from dotenv import load_dotenv
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Check your .env file.")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found. Check your .env file.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

search_tool = TavilySearchResults(
    max_results=3,
    tavily_api_key=TAVILY_API_KEY
)


class AgentState(TypedDict):
    topic: str
    research: str
    draft: str
    final_content: str


def researcher_agent(state: AgentState):
    topic = state["topic"]
    results = search_tool.invoke(topic)
    summary_prompt = f"Summarize these search results about '{topic}' in bullet points:\n{results}"
    summary = llm.invoke(summary_prompt).content
    return {"research": summary}


def writer_agent(state: AgentState):
    prompt = f"""Based on this research: {state['research']}
Write an engaging social media post about '{state['topic']}'.
Keep it under 150 words, catchy tone."""
    draft = llm.invoke(prompt).content
    return {"draft": draft}


def editor_agent(state: AgentState):
    prompt = f"""Review and improve this draft for grammar, tone, and impact:
{state['draft']}
Return only the final polished version."""
    final = llm.invoke(prompt).content
    return {"final_content": final}