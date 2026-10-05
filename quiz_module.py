def generate_quiz(
    client,
    model,
    topic,
    number_of_questions,
    difficulty
):

    prompt = f"""
You are EduGenie AI.

Create a multiple-choice quiz.

Topic:
{topic}

Number of questions:
{number_of_questions}

Difficulty:
{difficulty}

For every question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Make every question different.
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text