
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Thukuna AI",
    page_icon="⚡"
)

st.title("⚡ THUKUNA AI")
st.caption("Your personal AI assistant")

client = OpenAI()

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
            response = client.responses.create(
                model="gpt-4.1-mini",
                instructions="You are Thukuna AI, a helpful and intelligent assistant.",
                input=st.session_state.messages
            )

            answer = response.output_text
            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
