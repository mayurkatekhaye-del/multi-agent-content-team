from langgraph.graph import StateGraph, END
from agents import AgentState, researcher_agent, writer_agent, editor_agent


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("researcher", researcher_agent)
    workflow.add_node("writer", writer_agent)
    workflow.add_node("editor", editor_agent)

    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "editor")
    workflow.add_edge("editor", END)

    return workflow.compile()


app = build_graph()