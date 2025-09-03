from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph , START ,END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.schema import SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langgraph.checkpoint.mongodb import MongoDBSaver

import os  
load_dotenv()
import subprocess
SYSTEM_PROMPT ="""
     You are an intelligent agent coding assistant that helps in user coding query by using the right set of commands and right set of tools provided to you , you mainly work inside ./cursor directory and make files inside it only . 
    Always before proceeding with writing in file always read if the file is available and what are text content
    ,same goes for your current directory given in the earlier instruction or the new ones you will create based on user requirements                          
"""

MONGODB_URL = 'mongodb://admin:admin@localhost:27017'

llm = init_chat_model(model_provider='openai',model='gpt-4.1')

@tool
def command_tool(command: str) -> str:
    """Run commands on the user terminal and return stdout + stderr."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr


class State(TypedDict):
    messages:Annotated[list,add_messages]

available_tools = [command_tool]

llm_with_tools = llm.bind_tools(tools=available_tools)


toolnode = ToolNode(tools=available_tools)

def chat_node(state:State):
    system_message = SystemMessage(content=SYSTEM_PROMPT)
    
    response = llm_with_tools.invoke([system_message]+state["messages"])

    return {
        "messages":[response]
    }



    


graph_builder = StateGraph(State)

graph_builder.add_node('chat_node',chat_node)
graph_builder.add_node('tools',toolnode)

graph_builder.add_edge(START,"chat_node")
graph_builder.add_conditional_edges("chat_node",tools_condition)
graph_builder.add_edge('tools',"chat_node")
graph_builder.add_edge("chat_node",END)



def compile_with_checkpointer(checkpointer,graph_builder):
    graph = graph_builder.compile(checkpointer=checkpointer)
    return graph



    





    

