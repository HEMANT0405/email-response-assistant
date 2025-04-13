from openai import OpenAI

# Use your API key
client = OpenAI(api_key=api_key)

# Then update your generate_reply function:
def generate_reply(subject, body, tone_style):
    prompt = f"""You are an AI assistant that crafts replies to emails.
Email Subject: {subject}
Email Body: {body}

Write a reply with a {tone_style} tone."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful assistant for email replies."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )
    return response.choices[0].message.content
