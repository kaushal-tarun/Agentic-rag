from langgraph.graph import StateGraph, END
from backend.agents.agent import AgentState
from backend.tools.calculator import calculator


def chatbot(state: AgentState):
    message = state["message"]

    if any(op in message for op in ["+", "-", "*", "/"]):
        result = calculator(message)

        return {
            "response": f"Calculator Result: {result}"
        }

    return {
        "response": f"You said: {message}"
    }

def router(state: AgentState):
    message = state["message"]

    if any(op in message for op in ["+", "-", "*", "/"]):
        return {
            "route": "calculator"
        }

    return {
        "route": "chat"
    }

graph = StateGraph(AgentState)

graph.add_node("chatbot", chatbot)

graph.set_entry_point("chatbot")

graph.add_edge("chatbot", END)

agent = graph.compile()