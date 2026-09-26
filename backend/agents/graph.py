from langgraph.graph import StateGraph, END
from backend.agents.agent import AgentState


def chatbot(state: AgentState):
    return {
        "response": f"You said: {state['message']}"
    }


graph = StateGraph(AgentState)

graph.add_node("chatbot", chatbot)

graph.set_entry_point("chatbot")

graph.add_edge("chatbot", END)

agent = graph.compile()