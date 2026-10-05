def explain_topic(client, model, topic, level):

    prompt = f"""
You are EduGenie AI, a helpful educational tutor.

Explain the topic clearly for a student at the specified level.

Topic:
{topic}

Student level:
{level}

Use student-friendly language, define important terms, explain the key ideas step by step, and include a relevant example. Adjust the depth and vocabulary to the student's level.
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text