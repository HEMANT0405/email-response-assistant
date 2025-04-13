import streamlit as st
import openai
import os

# Load your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Or hardcode it temporarily for testing

st.set_page_config(page_title="Email Response Assistant", page_icon="📧")
st.title("📨 Email Response Assistant")
st.write("Easily generate email replies using AI!")

# User input
email_content = st.text_area("📩 Paste the received email here:", height=200)

tone = st.selectbox(
    "🎯 Choose the tone of your response:",
    ["Formal", "Friendly", "Apologetic", "Enthusiastic", "Neutral"]
)

if st.button("✉️ Generate Response"):
    if not email_content.strip():
        st.warning("Please enter the email content.")
    else:
        with st.spinner("Generating your reply..."):
            prompt = (
                f"You are an AI email assistant. Write a {tone.lower()} email reply "
                f"to the following message:\n\n\"{email_content}\""
            )

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=300,
                    temperature=0.7
                )

                reply = response.choices[0].message["content"]
                st.success("✅ Response Generated:")
                st.text_area("📨 Suggested Reply:", reply, height=200)

            except Exception as e:
                st.error(f"Error: {e}")
