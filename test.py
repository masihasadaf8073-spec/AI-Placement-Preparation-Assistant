from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    "gemini-3.5-flash",
    model_provider="google_genai"
)

result = model.invoke(
    "What are models in GenAI? Explain in one sentence."
)

print(result.content)