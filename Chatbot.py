import streamlit as st
import os
from openai import OpenAI



openai_api_key=os.getenv("OPENAI_API_KEY")
# Create an OpenAI client instance using the API key from the .env file



with st.sidebar:
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
   
    
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/rehabreda/GPT-Clone)"


conversation_history = []

def chat_with_gpt_stream(prompt, model="gpt-3.5-turbo", temperature=0.7):
    try:
        # Add the new user message to the conversation history
        conversation_history.append({"role": "user", "content": prompt})

        # Limit the history length based on the environment variable
        max_history = int(os.getenv("MAX_HISTORY_LENGTH", 5))
        messages_to_send = conversation_history[-max_history:]

        # Create a chat completion using the OpenAI client
        stream = client.chat.completions.create(
            messages=messages_to_send,
            model=model,
            temperature=temperature,
            stream=True,
        )
        # Extract and return the response content
        return stream
    except Exception as e:
        # Return the error message if an exception occurs
        return str(e)
    

st.title("GPT Clone")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
