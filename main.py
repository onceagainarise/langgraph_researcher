from dotenv import load_dotenv
from typing import Annotated, List
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
import os
from langchain_groq import ChatGroq
from web_operations import serp_search

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),    
               model="deepseek-r1-distill-llama-70b",
               temperature=0.7)

class State(TypedDict):
  messages: Annotated[list, add_messages]
  user_question: str | None
  google_results: str | None
  bing_results: str | None
  reddit_results: str | None
  selected_reddit_urls: list[str] | None
  reddit_post_data: str | None
  google_analysis: str | None
  bing_analysis: str | None
  reddit_analysis: str | None
  final_answer: str | None

def google_search(state: State):
  # Placeholder for Google Search API call
  user_question = state.get("user_question", "")
  print(f"Performing Google search for: {user_question}")
  google_results=serp_search(user_question,engine="google")
  
  return {"google_results": google_results}

def bing_search(state: State):
   # Placeholder for Bing Search API call
  user_question = state.get("user_question", "")
  print(f"Performing Bing search for: {user_question}")
  bing_results=serp_search(user_question,engine="bing")
  
  return {"bing_results": bing_results}
 
def reddit_search(state: State):
  # Placeholder for Reddit Search API call
  user_question = state.get("user_question", "")
  print(f"Performing Reddit search for: {user_question}")
  reddit_results=[]
  return {"reddit_results": reddit_results}

def analyze_reddit_posts(state: State):
  # Placeholder for Reddit post analysis
  return {"selected_reddit_urls": []}
  return  
def retrieve_reddit_posts(state: State):
  # Placeholder for retrieving Reddit posts
  return {"reddit_post_data": ""}
def analyze_google_results(state: State):
  # Placeholder for analyzing Google results
  return {"google_analysis": ""}
def analyze_bing_results(state: State):
  # Placeholder for analyzing Bing results
  return {"bing_analysis": ""}
def analyze_reddit_results(state: State):
  # Placeholder for analyzing Reddit results
  return {"reddit_analysis": ""}
def synthesize_analyses(state: State):
  # Placeholder for synthesizing information
  return {"final_answer": ""}

graph_builder = StateGraph(State)
graph_builder.add_node("google_search", google_search)
graph_builder.add_node("bing_search", bing_search)
graph_builder.add_node("reddit_search", reddit_search)      
graph_builder.add_node("analyze_reddit_posts", analyze_reddit_posts)      
graph_builder.add_node("retrieve_reddit_posts", retrieve_reddit_posts)      
graph_builder.add_node("analyze_google_results", analyze_google_results)    
graph_builder.add_node("analyze_bing_results", analyze_bing_results)
graph_builder.add_node("analyze_reddit_results", analyze_reddit_results)
graph_builder.add_node("synthesize_analyses", synthesize_analyses)


graph_builder.add_edge(START, "google_search")
graph_builder.add_edge(START, "bing_search")
graph_builder.add_edge(START, "reddit_search")
graph_builder.add_edge("google_search", "analyze_reddit_posts")
graph_builder.add_edge("bing_search", "analyze_reddit_posts")
graph_builder.add_edge("reddit_search", "analyze_reddit_posts")

graph_builder.add_edge("retrieve_reddit_posts", "analyze_google_results")
graph_builder.add_edge("retrieve_reddit_posts", "analyze_bing_results")
graph_builder.add_edge("retrieve_reddit_posts", "analyze_reddit_results")

graph_builder.add_edge("analyze_google_results", "synthesize_analyses")
graph_builder.add_edge("analyze_bing_results", "synthesize_analyses")
graph_builder.add_edge("analyze_reddit_results", "synthesize_analyses")

graph_builder.add_edge("synthesize_analyses", END)

graph=graph_builder.compile()

def run_chatbot():
  print("langgraph Agent")
  print("Type 'exit' to quit\n")

  while True:
    user_input = input("Ask me anything: ")
    if user_input.lower() == 'exit':
      break
    state = {
      "messages": [{"role": "user", "content": user_input}],
      "user_question": user_input,
      "google_results": None,
      "bing_results": None,
      "reddit_results": None,
      "selected_reddit_urls": None,
      "reddit_post_data": None,
      "google_analysis": None,
      "bing_analysis": None,
      "reddit_analysis": None,
      "final_answer": None
    }
    print("Processing...\n")
    final_state = graph.invoke(state)
    if final_state.get("final_answer"):
      print(f"Answer:\n {final_state.get('final_answer')}\n")
    print("-"*150)
if __name__ == "__main__":
  run_chatbot()