from chatgpt import Conversation
import streamlit as st

# Create a text input for the first field
input1 = st.text_input("Enter some text:")

# Create a text input for the second field
input2 = st.text_input("Enter some more text:")

# Show the inputs on the page
st.write("Input 1: ", input1)
st.write("Input 2: ", input2)


conversation = Conversation()
st.write(
    conversation.chat(
        "We are going to start a conversation. "
        "I will speak English and you will speak Portuguese."
    )
)
st.write(conversation.chat("What's the color of the sky?"))

# The AI will forget it was speaking Portuguese
conversation.reset()
st.write(conversation.chat("What's the color of the sun?"))

