from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Default standard Groq model
    api_key=os.getenv("GROQ_API_KEY")
)

print("AI Chatbot Started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = llm.invoke(user_input)

    print("AI:", response.content)
