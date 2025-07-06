import streamlit as st
from main import get_gemini_response
from google.genai import types

st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini Chatbot")
st.markdown("Chat with Google Gemini")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Create input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    reply, updated_history = get_gemini_response(st.session_state.history, user_input)
    st.session_state.history = updated_history

# Optional: Clear Chat
if st.button("Clear Chat"):
    st.session_state.history = []

# Display conversation
st.markdown("### 💬 Chat History")
for msg in st.session_state.history:
    if msg.role == "user":
        st.markdown(f"**🧑 You:** {msg.parts[0].text}")
    elif msg.role == "model":
        st.markdown(f"**🤖 Gemini:** {msg.parts[0].text}")
