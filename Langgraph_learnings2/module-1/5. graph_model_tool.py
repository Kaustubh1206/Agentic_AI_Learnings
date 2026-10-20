from typing import Annotated, NotRequired , List
from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from langchain.tools import tool

load_dotenv()

model_llm=ChatOpenAI(model="gpt-6-luna")

# Tool 
@tool
def multiply(nb1:int , nb2:int)->int:
    """This tool is used for multiplying 2 numbers and returning the product"""
    return nb1*nb2


model_llm_with_tool=model_llm.bind_tools([multiply])

# State

class MessagesState(TypedDict):
    # Add messages telling add messages to the list ( merged 2 list of messages)
    messages: Annotated[List[AnyMessage],add_messages]


# Nodes
def chat_with_tool(state: MessagesState) -> MessagesState:
    # reply to the list of messages that i gave you 
    return {"messages":[model_llm_with_tool.invoke(state["messages"])]}


builder=StateGraph(MessagesState) 

# Nodes 

builder.add_node("chat_with_tool",chat_with_tool)


# edges

builder.add_edge(START,"chat_with_tool")
builder.add_edge("chat_with_tool",END)

graph=builder.compile()