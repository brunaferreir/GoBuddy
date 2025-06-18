import streamlit as st 
from chatbot_logic import initialize_gemini_chat, get_gemini_response
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="GoBuddy: Seu Assistente de Go Básico",
    page_icon="🌌",
    layout="centered"
)
st.title("GoBuddy: Seu Assistente de Go Básico 🌌")
st.write("Pergunte-me qualquer coisa sobre os fundamentos de Go (Golang) e eu tentarei te ajudar!")


if "chat_session" not in st.session_state:
    try:
        st.session_state.chat_session = initialize_gemini_chat()
        st.session_state.messages = [
            {"role": "assistant", "content": "Olá! Sou seu GoBuddy. Qual sua primeira dúvida sobre Go?"}
        ]
    except ValueError as e:
        st.error(f"Erro de configuração: {e}. Verifique se sua GEMINI_API_KEY está configurada corretamente.")
        st.stop() 


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_input := st.chat_input("Pergunte algo sobre Go..."):
   
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

  
    with st.spinner("GoBuddy está pensando..."):
        gemini_response = get_gemini_response(st.session_state.chat_session, user_input)

   
    st.session_state.messages.append({"role": "assistant", "content": gemini_response})
    with st.chat_message("assistant"):
        st.markdown(gemini_response)


if st.button("Reiniciar Conversa 🔄"):
    st.session_state.chat_session = initialize_gemini_chat()
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Sou seu GoBuddy. Qual sua primeira dúvida sobre Go?"}
    ]
    st.rerun() 