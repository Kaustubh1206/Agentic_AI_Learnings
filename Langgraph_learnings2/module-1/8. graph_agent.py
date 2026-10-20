from typing import Annotated, NotRequired , List
from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AnyMessage, SystemMessage
from langgraph.graph.message import add_messages, MessagesState
from langchain.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
load_dotenv()

model_llm=ChatOpenAI(model="gpt-6-luna")


@tool
def multiply(nb1: int, nb2:int)-> int:
    """This tool returns multiplication of 2 numbers"""
    return nb1*nb2


@tool
def addition(nb1: int, nb2:int)-> int:
    """This tool returns addition of 2 numbers"""
    return nb1+nb2

@tool
def substraction(nb1: int, nb2:int)-> int:
    """This tool returns substraction of 2 numbers"""
    return nb1-nb2

@tool
def multiply(nb1: int, nb2:int)-> int:
    """This tool returns multiplication of 2 numbers"""
    return nb1* nb2

model_llm_with_tools=model_llm.bind_tools([multiply,addition,substraction])

system_message=SystemMessage(content="You are a helpful mathematics teacher")

# Nodes
def chat_with_tools(state: MessagesState) -> MessagesState:
    return {"messages":[model_llm_with_tools.invoke(state['messages']+[system_message])]}

builder=StateGraph(MessagesState)


builder.add_node("chat_with_tools",chat_with_tools)
builder.add_node("tools",ToolNode([multiply,addition,substraction]))

builder.add_edge(START,"chat_with_tools")
builder.add_conditional_edges("chat_with_tools",tools_condition)
builder.add_edge("tools",END)

graph=builder.compile()


