from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from typing import TypedDict,List

from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    messages: List[HumanMessage]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state['messages'])
    print(f"\nAI:{response.content}")
    return state

graph=StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent_bot=graph.compile()

user_input = input("Enter: ")
while user_input!="exit":
    agent_bot.invoke({"messages":[HumanMessage(content=user_input)]})
    user_input = input("Enter: ")
