import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

# Page title
st.set_page_config(page_title="Email Response Assistant", page_icon="📧")
st.title("📧 Email Response Assistant")

# Input fields
email_input = st.text_area("✉️ Paste the email you received:")
tone = st.selectbox("🎯 Choose response tone:", ["Formal", "Informal", "Friendly", "Professional"])

# Button to generate response
if st.button("Generate Reply"):
    if email_input.strip() == "":
        st.warning("Please enter an email to generate a reply.")
    else:
        with st.spinner("Generating reply..."):
            prompt = f"Write a {tone.lower()} reply to the following email:\n\n{email_input}"
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                reply = response.choices[0].message.content
                st.subheader("📨 AI-Generated Reply:")
                st.write(reply)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
