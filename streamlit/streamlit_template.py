import streamlit as st
from streamlit_chat import message
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from credentials import api_key
import openai


# ----------------- STREAMLIT APP ----------------- #
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


# ----------------- FUNCTIONS ----------------- #
def load_chain():
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature=0, openai_api_key=api_key)
    chain = ConversationChain(llm=llm)
    return chain


def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text


chain = load_chain()
user_input = get_text()

# Add a button to submit the user input
# ----------------- INTERACTIONS ----------------- #
if user_input:
    output = chain.run(input=user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:

    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")