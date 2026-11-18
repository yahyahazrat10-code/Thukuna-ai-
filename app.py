
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="THUKUNA AI",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ THUKUNA AI")
st.caption("Your personal AI assistant")

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Talk to Thukuna..."):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thukuna is thinking..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are Thukuna AI, a helpful, intelligent and friendly assistant."
                        },
                        *st.session_state.messages
                    ]
                )

                answer = response.choices[0].message.content
                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Thukuna error: {e}")
