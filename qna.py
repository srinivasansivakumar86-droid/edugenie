def answer_question(client, model, question):

    prompt = f"""
You are EduGenie AI, a helpful educational assistant.

Answer the student's question clearly.

Student question:
{question}

Requirements:
- Use simple student-friendly language.
- Explain step by step.
- Give examples where useful.
- Include important points.
- Do not unnecessarily complicate the answer.
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text