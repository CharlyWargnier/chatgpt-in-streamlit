import streamlit as st
from chatgpt import Conversation

c1, c2 = st.columns([0.4, 2])

with c1:

    # Add a logo to the sidebar
    st.image("logo.png", width=150)

with c2:

    # Set the title
    st.title("ChatGPT in Streamlit")


with st.form("my_form"):

    # Create a text input for the first field
    input1 = st.text_input("Enter some instructions below:")

    # Create a text input for the second field
    input2 = st.text_input("Enter secondary text, if needed")

   # Every form must have a submit button.
    submitted = st.form_submit_button("🤖 Submit")

if submitted:
    # st.write("slider", slider_val, "checkbox", checkbox_val)

    conversation = Conversation()
    st.write(
        conversation.chat(input1)
    )
    st.write(conversation.chat(input2))

    # The AI will forget it was speaking Portuguese
    conversation.reset()

    st.stop()
