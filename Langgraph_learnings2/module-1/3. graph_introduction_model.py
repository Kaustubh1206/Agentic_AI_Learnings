from typing import NotRequired
from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# State

class State(TypedDict):
    graph_int:NotRequired[int]
    graph_str:str

# Nodes

model_llm=ChatOpenAI(model="gpt-6-luna")

# Node 1 
def node1(state: State) -> State:
    """"Take a state and ask our model to pick a number between 2 or 3"""
    model_response=model_llm.invoke("Can you choose between 2 or 3. Reply only with a number")
    if isinstance(int(model_response.content), int):
        return {"graph_int":int(model_response.content),
                "graph_str":state["graph_str"] + "passed by node 1"}
    return {"graph_int": 0,
                "graph_str":state["graph_str"] + "passed by node 1"}


def node2(state: State) -> State:
    """"Take a state and ask our model to pick a number between 1 or 2"""
    return {"graph_int": state["graph_int"], "graph_str":state["graph_str"] + "passed by node 2"}



def node3(state: State) -> State:
    """"Take a state and ask our model to pick a number between 1 or 2"""
    return {"graph_int": state["graph_int"], "graph_str":state["graph_str"] + "passed by node 3"}

# Create Edges 

def next_step(state: State) -> Literal["node2", "node3",END]:
    """Check state and the return which node to go"""
    number_state=state["graph_int"]
    if number_state ==2:
        return "node2"
    elif number_state==3:
        return "node3"
    
    else :
        return END
    

# Putting all together
builder=StateGraph(State) 

# build nodes

builder.add_node("node1",node1)
builder.add_node("node2",node2)
builder.add_node("node3",node3)


# building 
builder.add_edge(START,"node1")
builder.add_conditional_edges("node1",next_step)
builder.add_edge("node2",END)
builder.add_edge("node3",END)


graph=builder.compile()

