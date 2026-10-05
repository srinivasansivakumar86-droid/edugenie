def summarize_text(client, model, text):

    prompt = f"""
You are EduGenie AI.

Summarize the following study material.

Study material:
{text}

Provide:

- Main ideas
- Important definitions
- Key points
- Important facts
- Exam-oriented notes
- Short revision summary

Use clear bullet points.
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text