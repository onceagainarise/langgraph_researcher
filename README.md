# LangGraph Multi-Source Research Agent

This project is an advanced research assistant that performs parallel web searches (Google, Bing, Reddit), analyzes the results, and synthesizes a final answer using a Groq-hosted LLM. It is built with [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://github.com/langchain-ai/langchain), and [langchain_groq](https://pypi.org/project/langchain-groq/).

## Features
- **Parallel Search:** Simultaneously queries Google, Bing, and Reddit for a user-supplied question.
- **Reddit Post Analysis:** Selects and retrieves relevant Reddit posts and comments for deeper analysis.
- **Automated Analysis:** Uses an LLM to analyze search results from each source.
- **Synthesis:** Combines all analyses into a final, comprehensive answer.
- **Interactive CLI:** Run as a chatbot in your terminal.
- **Modular Graph Workflow:** Easily extend or modify the research pipeline using LangGraph's node/edge system.

## File Structure
- `main.py` — Main pipeline, graph definition, and CLI chatbot.
- `web_operations.py` — Functions for web search and Reddit data retrieval.
- `prompts.py` — Prompt templates for LLM analysis (not shown here, but referenced in code).

## Requirements
- Python 3.9+
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- [langchain_groq](https://pypi.org/project/langchain-groq/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)

## Setup
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd langgraph_project_1
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   Create a `.env` file in the project root with your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key
   # Add other API keys as needed for search APIs
   ```

## Usage
Run the chatbot from your terminal:
```sh
python main.py
```
Type your research question and the agent will perform multi-source research and return a synthesized answer.

## Customization
- **Search APIs:**
  - The current implementation in `web_operations.py` uses Bright Data for search, which may not work (404 error). You should update it to use a working search API (e.g., SerpAPI, Bing Web Search, or another provider).
- **Prompts:**
  - You can customize the prompt templates in `prompts.py` to change how the LLM analyzes and synthesizes information.
- **Graph Workflow:**
  - Add or remove nodes/edges in `main.py` to change the research pipeline.

## Example Flow
1. User enters a question.
2. Google, Bing, and Reddit are searched in parallel.
3. Reddit results are analyzed to select relevant URLs.
4. Reddit posts/comments are retrieved and analyzed.
5. Google and Bing results are analyzed.
6. All analyses are synthesized into a final answer.

## License
MIT
