from langgraph.graph import START, END , StateGraph
from dotenv import load_dotenv
from typing_extensions import TypedDict

from asyncio import graph

# State 
class State(TypedDict):
    graph_str:str

# Node 
def greeting (state:State) -> State:
    """"Function takes a dict and returns a dict """ 
    return {"graph_str": state["graph_str"]+" welcome to learnings"}

# Edges 


# putting together 

builder=StateGraph(State)

# Add nodes
builder.add_node("greeting",greeting)

#  Add edges

builder.add_edges(START,"greeting")
builder.add_edges("greeting",END)


graph=builder.compile()


graph.invoke()