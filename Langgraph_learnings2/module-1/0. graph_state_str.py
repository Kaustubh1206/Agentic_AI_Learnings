# importing library 
from langgraph.graph import StateGraph , START ,END

# State - simple graph . String already created

# Nodes
def greeting(state: str) ->str:
    """This funciton greet people to Learnings"""
    return state + " welcome to AI carrer Lab"

# Edges - no smart edges 
# Simple edges not needed to define already defined


# langgraph putting our graph together

builder = StateGraph(str)

# add nodes to our graph
builder.add_node("greeting",greeting)

# add edges
builder.add_edge(START,"greeting")
builder.add_edge("greeting",END)


graph = builder.compile()

# print(graph.invoke("Hey am new!"))
