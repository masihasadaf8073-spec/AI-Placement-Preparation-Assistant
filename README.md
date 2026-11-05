# AI Placement Preparation Assistant

An AI-powered interview preparation application built using Python, LangChain, OpenRouter and Streamlit.

## Features
- Modern, responsive interface with a focused interview-preparation dashboard
- Role-based interview preparation
- Experience-level selection
- Custom difficulty selection
- AI-generated interview questions
- Model answers and explanations
- Practical examples and follow-up questions
- Question sets organized with role, experience, question-count, type and difficulty details

## Technologies
- Python
- LangChain
- OpenRouter
- Pydantic
- Streamlit

## Installation

1. Create a virtual environment.
2. Install dependencies:

   pip install -r requirements.txt

3. Create a `.env` file by copying `.env.example`, then add your OpenRouter and
   LangSmith API keys:

   ```powershell
   Copy-Item .env.example .env
   ```

   Replace both placeholder API keys with your own. LangSmith tracing is enabled
   for the `task` project. `MODEL_NAME` is optional; it defaults to
   `openai/gpt-4o-mini`. Keep `.env` private and do not commit it.

4. Run the application:

   streamlit run app.py