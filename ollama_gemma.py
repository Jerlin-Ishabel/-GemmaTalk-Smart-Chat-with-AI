from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="💬 Chatbot", layout="wide")
st.title("🧠 LangChain + Ollama Chatbot")
st.write("Ask me anything and let's chat continuously!")

# Initialize Ollama model
llm = Ollama(model="gemma3:1b")  # or gemma:3b if downloaded
parser = StrOutputParser()

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("Type your message here...")

if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Build prompt from history
    messages = [("system", "You are a helpful assistant. Answer clearly and concisely.")]
    for msg in st.session_state.chat_history:
        messages.append((msg["role"], msg["content"]))

    prompt = ChatPromptTemplate.from_messages(messages)
    chain = prompt | llm | parser

    # Generate AI response
    response = chain.invoke({"question": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display chat with bubbles
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"""
        <div style='text-align: right; margin: 10px;'>
            <span style='background-color: #DCF8C6; padding: 8px 12px; border-radius: 15px; display: inline-block;'>
                {chat['content']}
            </span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='text-align: left; margin: 10px;'>
            <span style='background-color: #F1F0F0; padding: 8px 12px; border-radius: 15px; display: inline-block;'>
                {chat['content']}
            </span>
        </div>
        """, unsafe_allow_html=True)
