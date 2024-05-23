import streamlit as st
import openai

import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: repeat;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('teste.png')

def get_bot_response(user_message):
    if user_message=="Ola":
        return "tas bom?"
    return f"Esta é uma resposta do chatbot para: {user_message}"

# Define the image URL
image_url = "/home/jbtescudeiro16/4ANO2SEM/DataMining/Frontend/logo.png"
st.sidebar.image(image_url, use_column_width=True)

image_url = "/home/jbtescudeiro16/4ANO2SEM/DataMining/Frontend/image.png"
col1, col2, col3 = st.columns([1.3, 5, 0.2])
col2.image(image_url,width= 400)


if "messages" not in st.session_state:
    st.session_state.messages=[]

#display chat history
st.markdown(
            """
        <style>
            .st-emotion-cache-1c7y2kd {
                flex-direction: row-reverse;
                text-align: right;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )

for message in st.session_state.messages:
    if message['role']== "user":
        av = "🙍‍♂️"
    else:
        av= "🤖"

    with st.chat_message(message["role"],avatar=av):
        st.write(message["content"])




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