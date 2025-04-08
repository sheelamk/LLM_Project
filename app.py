import streamlit as st
from groq import Groq

# Load GROQ_API_KEY from secrets.toml (local and Streamlit Cloud)
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("❌ GROQ_API_KEY not found. Please check your secrets.toml file or Streamlit Secrets.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Streamlit UI Setup
st.set_page_config(page_title="StratoBot", layout="centered")
st.title("⚡ StratoBot")
st.caption("Powered by Groq API | Multi-Model Chat App")

# Sidebar Settings
available_models = [
    "llama3-70b-8192",
    "llama3-8b-8192",
    "llama2-70b-4096"
]
model = st.sidebar.selectbox("⚙️ Choose a model", available_models)
temperature = st.sidebar.slider("🎛 Temperature", 0.0, 1.0, 0.7, 0.1)

# Session State Setup
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display Chat History
for msg in st.session_state["messages"][1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
prompt = st.chat_input("Type your message here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Make API call using Groq client
    try:
        chat_completion = client.chat.completions.create(
            messages=st.session_state["messages"],
            model=model,
            temperature=temperature
        )

        reply = chat_completion.choices[0].message.content

        # Token usage details
        usage = chat_completion.usage
        prompt_tokens = usage.prompt_tokens
        completion_tokens = usage.completion_tokens
        total_tokens = usage.total_tokens

        st.chat_message("assistant").markdown(reply)
        st.session_state["messages"].append({"role": "assistant", "content": reply})

        # Token Usage Display
        with st.sidebar:
            st.subheader("🔩 Token Usage")
            st.write(f"**Prompt Tokens:** {prompt_tokens}")
            st.write(f"**Completion Tokens:** {completion_tokens}")
            st.write(f"**Total Tokens:** {total_tokens}")

    except Exception as e:
        st.error(f"❗ Error: {e}")
