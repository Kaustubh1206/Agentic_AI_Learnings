from typing import Annotated, NotRequired , List
from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

load_dotenv()


# State

class MessagesState(TypedDict):
    # Add messages telling add messages to the list ( merged 2 list of messages)
    messages: Annotated[List[AnyMessage],add_messages]


model_llm = ChatOpenAI(model="gpt-6-luna")


# Nodes 

def chat(state : MessagesState) -> MessagesState:
    # Here we are taking a state and returning a state
    # Eg - Human message -> What is color of sky -> llm
    # 
    # Ai message -> Sky color is blue 
    return {"messages":[model_llm.invoke(state["messages"])]}


# Edge

# Creat our groah

builder=StateGraph(MessagesState)

# build node 
builder.add_node("chat",chat)

# build edges
builder.add_edge(START,"chat")
builder.add_edge("chat",END)


graph = builder.compile()
