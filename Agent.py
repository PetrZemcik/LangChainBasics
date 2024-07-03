# Import relevant functionality
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import create_react_agent

import os
from dotenv import load_dotenv
load_dotenv()
anthropic_api_key=os.getenv('ANTHROPIC_API_KEY')
print(anthropic_api_key)

# Create the agent
memory = SqliteSaver.from_conn_string(":memory:")
model = ChatAnthropic(model_name="claude-3-sonnet-20240229")
search = TavilySearchResults(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
config = {"configurable": {"thread_id": "abc123"}}
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="hi. I am Petr and conduct research regarding companies.")]}, config
):
    print(chunk)
    print("----")

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="what can you tell me about Tesla?")]}, config
):
    print(chunk)
    print("----")