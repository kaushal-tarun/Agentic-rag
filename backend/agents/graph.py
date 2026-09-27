from langgraph.graph import StateGraph, END
from backend.agents.agent import AgentState
from backend.tools.calculator import calculator
from backend.services.gemini_service import decide_route

def chat_node(state: AgentState):
    return {
        "response": f"You said: {state['message']}"
    }



def router(state: AgentState):
    decision = decide_route(state["message"])

    return {
        "route": decision.route
    }


def calculator_node(state: AgentState):
    result = calculator(state["message"])

    return {
        "response": f"Calculator Result: {result}"
    }


graph = StateGraph(AgentState)

graph.add_node("router", router)
graph.add_node("calculator", calculator_node)
graph.add_node("chat", chat_node)

graph.set_entry_point("router")


def route_decision(state: AgentState):
    return state["route"]


graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "calculator": "calculator",
        "chat": "chat",
    },
)

graph.add_edge("calculator", END)
graph.add_edge("chat", END)

agent = graph.compile()