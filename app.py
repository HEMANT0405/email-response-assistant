from openai import OpenAI

# Use your API key
client = OpenAI(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)

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
