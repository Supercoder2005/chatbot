# main.py (a.k.a chatbot_gemini.py)

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Set the model to use
model = "gemini-2.0-flash"

# Set up configuration
generate_content_config = types.GenerateContentConfig(
    response_mime_type="text/plain",
)

# 🔁 CLI Chatbot Function
def chat():
    print("Gemini Chatbot (type 'exit' to quit)")
    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break

        reply, history = get_gemini_response(history, user_input)
        print(f"Chatbot: {reply}")

# ✅ Add this function for UI reuse
def get_gemini_response(history, user_input):
    history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

    response = client.models.generate_content(
        model=model,
        contents=history,
        config=generate_content_config,
    )

    bot_reply = response.text.strip()

    history.append(types.Content(role="model", parts=[types.Part(text=bot_reply)]))

    return bot_reply, history

# Entry point for CLI
if __name__ == "__main__":
    chat()
