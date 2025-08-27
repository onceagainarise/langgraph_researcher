# LangGraph Multi-Search & Analysis Project

This project demonstrates a multi-step information retrieval and analysis pipeline using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and Groq LLMs. It performs Google, Bing, and Reddit searches, analyzes the results, and synthesizes a final answer using an LLM.

## Features
- Parallel web search using Google, Bing, and Reddit
- Analysis of search results and Reddit posts
- Synthesis of information using a Groq-hosted LLM (e.g., Llama3, DeepSeek)
- Modular, graph-based workflow with LangGraph

## Requirements
- Python 3.9+
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [langchain_groq](https://pypi.org/project/langchain-groq/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)

## Setup
1. Clone this repository:
   ```sh
   git clone <your-repo-url>
   cd langgraph_project_1
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root with your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   # Optionally, add other API keys as needed
   ```

## Usage
Run the main script:
```sh
python main.py
```

## File Structure
- `main.py` — Main pipeline and graph definition
- `web_operations.py` — Web search and API integration functions

## Notes
- You may need to update the search API integration in `web_operations.py` to use a working search API (e.g., SerpAPI, Bing Web Search, or another provider).
- The project is modular and can be extended with additional nodes or analysis steps.

## License
MIT
