import streamlit as st
import google.generativeai as genai

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Email Response Assistant",
    page_icon="📧",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---- SIDEBAR ----
st.sidebar.header("🔐 Gemini API Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")
st.sidebar.markdown("---")
st.sidebar.info("💡 This assistant generates email responses using Gemini AI. Choose a tone, input your email, and get a professional reply!")

# ---- MAIN HEADER ----
st.title("📬 Email Response Assistant")
st.markdown("Generate smart, professional replies to emails with AI assistance.")

# ---- INPUT FORM ----
with st.form("email_form"):
    subject = st.text_input("✉️ Email Subject")
    body = st.text_area("📄 Email Body (paste the message)", height=200)

    tone = st.selectbox("🎯 Select Response Tone", ["Professional", "Friendly", "Apologetic", "Assertive", "Custom"])
    custom_tone = ""
    if tone == "Custom":
        custom_tone = st.text_input("Enter Custom Tone")

    submit = st.form_submit_button("Generate Reply ✨")

# ---- FUNCTION ----
def generate_reply(subject, body, tone_style, api_key):
    import google.generativeai as genai
    genai.configure(api_key=api_key)

    prompt = f"""You are an AI assistant that crafts replies to emails.
Email Subject: {subject}
Email Body: {body}

Write a reply with a {tone_style} tone."""

    try:
        model = genai.GenerativeModel('models/gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ---- RESPONSE GENERATION ----
if submit:
    if not api_key:
        st.error("⚠️ Please enter your Gemini API key in the sidebar.")
    elif not subject or not body:
        st.warning("📭 Subject and body are required to generate a response.")
    else:
        style = custom_tone if tone == "Custom" else tone
        with st.spinner("Generating reply... ⏳"):
            reply = generate_reply(subject, body, style, api_key)
            if reply.startswith("❌ Error"):
                st.error(reply)
            else:
                st.success("✅ Response Generated")
                st.markdown("### 📩 Suggested Reply:")
                st.code(reply, language='markdown')
