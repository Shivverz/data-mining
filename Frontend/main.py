import streamlit as st
import openai


def get_bot_response(user_message):
    if user_message=="Ola":
        return "tas bom?"
    return f"Esta é uma resposta do chatbot para: {user_message}"

st.markdown("<h1 style='text-align: center; margin-top: -30px; color: green;'>FootDetective</h1>", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages=[]

#display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



prompt=st.chat_input("Enter your question here:")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    
    resposta=get_bot_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(resposta)

    st.session_state.messages.append({"role":"assistant","content":resposta})



if __name__ == "__main__":
    st.experimental_rerun()