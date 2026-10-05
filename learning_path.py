def create_learning_path(
    client,
    model,
    topic,
    level,
    duration
):

    prompt = f"""
You are EduGenie AI.

Create a personalized learning path.

Topic:
{topic}

Student level:
{level}

Duration:
{duration}

Include:

1. Prerequisites
2. Week-by-week learning plan
3. Important concepts
4. Practice activities
5. Mini projects
6. Revision plan
7. Final project
8. Expected skills

Make the plan realistic for a student.
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text