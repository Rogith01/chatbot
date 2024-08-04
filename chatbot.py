import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

tweet_prompt = PromptTemplate.from_template("{topic}.")

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

if __name__ == "__main__":
    st.title("Chatbot By Rogith")
    
    st.markdown("<div class='centered-container'><h3>Generate a Tweet on Your Favorite Topic!</h3></div>", unsafe_allow_html=True)
    
    # Text area for user to enter topic
    topic = st.text_area("", placeholder="Enter topic")

    # Center the button
    st.markdown("<div class='centered-button'>", unsafe_allow_html=True)
    if st.button("Generate Tweet"):
        # Generate response using LLMChain
        resp = tweet_chain.run(topic=topic)
        # Display response
        st.write("Generated Tweet:")
        st.markdown(f"<div style='padding: 20px; color:white; background-color: black; border-radius: 10px; border: 1px solid #ccc;'>{resp}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# Custom CSS to style the app
st.markdown("""
    <style>
    .main {
        background-color: black;
        padding: 20px;
        border-radius:10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
        width: auto;
    }
    .stButton button:hover{
        background-color:red;
        color:white;
    }
    .stTextArea textarea {
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ccc;
        width: 100%;
        height: 250px; /* Increased height */
        box-sizing: border-box;
    }
    h1, h3 {
        text-align: center;
        color: #4CAF50;
    }
    .centered-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .centered-button {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)