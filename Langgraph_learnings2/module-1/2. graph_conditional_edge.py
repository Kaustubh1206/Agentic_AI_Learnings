from langchain_protocol import StateCommand
from langgraph.graph import START, END , StateGraph
from typing_extensions import TypedDict
from typing import Literal

# State 
class State(TypedDict):
    graph_str: str 

# Nodes
def node1(state: State ) ->State:
    """This node Greet our user"""
    return {"graph_str": state["graph_str"]+ " Welcome to AI Learnings"}


def node2(state: State ) ->State:
    """This node Greet our user"""
    return {"graph_str": state["graph_str"]+ " I am in node 2"}

def node3(state: State ) ->State:
    """This node Greet our user"""
    return {"graph_str": state["graph_str"]+ " I am in node 3"}


# Edges - check state ask question  and conclude to conclusion that we can guide state

# We are going to take the state but we actually wants to returns which node is next .
def next_step(state: State) -> Literal["node2", "node3"]:
    """Guide the state/graph to next node"""
    state_str = state["graph_str"]
    array_state_str= state_str.split(" ")

    if array_state_str[0]=="hello":
        return "node2"
    
    return "node3"
# Putting graph together 

builder= StateGraph(State)

# Adding nodes
builder.add_node("node1",node1)
builder.add_node("node2",node2)
builder.add_node("node3",node3)

# Adding edges
builder.add_edge(START,"node1")
builder.add_conditional_edges("node1",next_step)
builder.add_edge("node2",END)
builder.add_edge("node3",END)

graph = builder.compile()