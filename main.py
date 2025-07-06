# chatbot_gemini.py

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# set the model to use
model = "gemini-2.0-flash"

# Set up configuration
generate_content_config = types.GenerateContentConfig(
    response_mime_type="text/plain",
)

# Start chatbot loop
def chat():
    print("Gemini Chatbot (type 'exit' to quit)")
    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break

        history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))

        # Generate Gemini response
        response = client.models.generate_content(
            model=model,
            contents=history,
            config=generate_content_config,
        )

        bot_reply = response.text.strip()
        print(f"Chatbot: {bot_reply}")

        # store bot's actual reply in history
        history.append(types.Content(role="model", parts=[types.Part(text=bot_reply)]))

if __name__ == "__main__":
    chat()
