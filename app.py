#app.py
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# --- Load API key from .env ---
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# --- Validate API key ---
if not groq_api_key:
    st.error("❌ GROQ_API_KEY not found. Please check your .env file.")
    st.stop()

# --- Initialize Groq client ---
client = Groq(api_key=groq_api_key)

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Groq LLM Chat", layout="centered")
st.title("🤖 Chat with Groq LLM")
st.caption("Powered by Groq API | Multi-Model Chat App")

# --- Sidebar Settings ---
available_models = [
    "llama-3.3-70b-versatile",  # Correct model name
]
model = st.sidebar.selectbox("🔍 Choose a model", available_models)
temperature = st.sidebar.slider("🎛 Temperature", 0.0, 1.0, 0.7, 0.1)

# --- Session State Setup ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# --- Display Chat History ---
for msg in st.session_state["messages"][1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat Input ---
prompt = st.chat_input("Type your message here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # --- Make API call using Groq client ---
    try:
        chat_completion = client.chat.completions.create(
            messages=st.session_state["messages"],
            model=model,
        )

        reply = chat_completion.choices[0].message.content

        st.chat_message("assistant").markdown(reply)
        st.session_state["messages"].append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"❌ Error: {e}")

# --- Token Usage Display ---
with st.sidebar:
    st.subheader("🧠 Token Usage")
    # You can still track the token usage if required
    st.write(f"**Prompt Tokens:** 0")  # Update based on actual tracking
    st.write(f"**Completion Tokens:** 0")  # Update based on actual tracking
    st.write(f"**Total Tokens:** 0")  # Update based on actual tracking



    
       
