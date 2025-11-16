🧠 LangChain + Ollama Chatbot

A smart, interactive chatbot built with **LangChain** and **Ollama Gemma 3B**, deployed using **Streamlit**. This chatbot allows users to have continuous conversations with AI, featuring **chat bubbles** and a **clear chat** experience.  

---

## Features

- **Interactive Chat:** Ask anything and get AI responses in real-time.
- **Persistent Conversation:** Maintains chat history during the session.
- **User-Friendly UI:** Alternating chat bubbles for user and AI messages.
- **Powered by AI:** Uses **LangChain** and **Ollama Gemma 3B** for accurate and concise answers.
- **Easy to Deploy:** Built entirely in Python with Streamlit.  

---

## Demo

<img width="1919" height="1073" alt="Screenshot 2025-11-16 213935" src="https://github.com/user-attachments/assets/3377faf0-b30f-4021-8144-eff24a2be22e" />

*Replace with your own screenshot showing the chat interface.*

---
Tools & Technologies Used

-Python 3.10+ – Core programming language for building the chatbot.

-Streamlit – Framework to create an interactive, web-based UI for the chatbot.

-LangChain – Provides the framework to create language model applications, including prompt handling and chaining.

-Ollama Gemma 3B – Large language model used for generating AI responses.

-python-dotenv – Manages environment variables like API keys securely.

Purpose of the Project

-The purpose of this project is to create a conversational AI chatbot that can:

-Assist users interactively – Answer questions clearly and concisely.

-Provide a smooth chat experience – Maintain conversation context and display messages in chat bubbles.

-Demonstrate AI integration – Show how LangChain and Ollama can be combined in a real-world application.

-Be easily deployable – Users can run it locally or on Streamlit Cloud with minimal setup.

How It Works

-User Input: The user types a message into the input box.

-Prompt Construction: The app dynamically builds a chat prompt using all previous messages in the session.

-AI Response: The Ollama Gemma 3B model generates a response based on the constructed prompt.

-Display: Both user messages and AI responses are displayed in alternating chat bubbles for clarity.

-Session Management: The conversation is stored in st.session_state to maintain context.



