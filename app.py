import streamlit as st

st.title("Simple AI Chatbot 🤖")

user_input = st.text_input("You:")

def get_reply(text):
    text = text.lower()

    if "hi" in text or "hello" in text:
        return "Hello! Kaise ho? 😊"
    elif "how are you" in text:
        return "Main theek hoon 😄 tum batao?"
    elif "name" in text:
        return "Main tumhara AI chatbot hoon 🤖"
    elif "2+2" in text:
        return "2+2 = 4"
    else:
        return "Samajh nahi aaya 😅 thoda aur clearly bolo"

if user_input:
    reply = get_reply(user_input)
    st.write("🤖 Bot:", reply)