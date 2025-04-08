import streamlit as st
import requests
import os
from dotenv import load_dotenv

# --- Load API key from .env ---
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# --- Validate API key ---
if not groq_api_key:
    st.error("❌ GROQ_API_KEY not found. Please check your .env file.")
    st.stop()

# --- API Settings ---
endpoint = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {groq_api_key}",
    "Content-Type": "application/json",
}

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Groq LLM Chat", layout="centered")
st.title("🤖 Chat with Groq LLM")
st.caption("Powered by Groq API | Multi-Model Chat App")

# --- Sidebar Settings ---
available_models = [
    "llama2-70b-chat",
    "mixtral-8x7b",
    "gemma-7b-it"
]
model = st.sidebar.selectbox("🔍 Choose a model", available_models)
temperature = st.sidebar.slider("🎛 Temperature", 0.0, 1.0, 0.7, 0.1)

# --- Session State Setup ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

if "token_usage" not in st.session_state:
    st.session_state["token_usage"] = {"prompt": 0, "completion": 0, "total": 0}

# --- Display Chat History ---
for msg in st.session_state["messages"][1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat Input ---
prompt = st.chat_input("Type your message here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    payload = {
        "model": model,
        "messages": st.session_state["messages"],
        "temperature": temperature,
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        reply = result["choices"][0]["message"]["content"]
        tokens = result.get("usage", {})

        st.chat_message("assistant").markdown(reply)
        st.session_state["messages"].append({"role": "assistant", "content": reply})

        # --- Update Token Stats ---
        st.session_state["token_usage"]["prompt"] += tokens.get("prompt_tokens", 0)
        st.session_state["token_usage"]["completion"] += tokens.get("completion_tokens", 0)
        st.session_state["token_usage"]["total"] += tokens.get("total_tokens", 0)

    except Exception as e:
        st.error(f"❌ Error: {e}")

# --- Token Usage Display ---
with st.sidebar:
    st.subheader("🧠 Token Usage")
    st.write(f"**Prompt Tokens:** {st.session_state['token_usage']['prompt']}")
    st.write(f"**Completion Tokens:** {st.session_state['token_usage']['completion']}")
    st.write(f"**Total Tokens:** {st.session_state['token_usage']['total']}")
