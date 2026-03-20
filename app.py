import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(prompt):
    chat = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )
    return chat.choices[0].message.content


st.title("🌆 AI Smart City Assistant")

st.caption("AI-powered solutions for sustainable cities 🌱")

feature = st.selectbox("Select Feature", [
    "Eco Tips Generator",
    "Govt Scheme Advisor",
    "Smart City Chatbot"
])

# ECO TIPS
if feature == "Eco Tips Generator":
    problem = st.text_input("Enter problem (e.g., air pollution)")

    if st.button("Generate Tips"):
        if problem:
           result = get_ai_response(f"Give eco-friendly solutions for {problem}")
           st.success(result)
        else:
            st.warning("Please enter a problem")
        
# GOVT SCHEMES
if feature == "Govt Scheme Advisor":
    city = st.selectbox("Select City", ["Delhi", "Mumbai"])
    group = st.text_input("Target group (students, farmers)")

    if st.button("Get Schemes"):
        if group:
            result = get_ai_response(f"Suggest government schemes in {city} for {group}")
        st.success(result)
    else:
        st.warning("Please enter target group")
# Chatbot Feature
if feature =="Smart City Chatbot":
    user_input = st.text_input("Ask anything about smart city")

    if st.button("Ask AI"):
        if user_input:
            result = get_ai_response(user_input)
            st.success(result)
        else:
            st.warning("Please enter a question")