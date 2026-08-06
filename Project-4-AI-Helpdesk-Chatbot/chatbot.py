import sqlite3
from difflib import get_close_matches


def get_response(user_question):

    conn = sqlite3.connect("helpdesk.db")
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM faq")

    data = cursor.fetchall()

    conn.close()

    questions = [row[0] for row in data]

    answers = {row[0]: row[1] for row in data}

    match = get_close_matches(
        user_question,
        questions,
        n=1,
        cutoff=0.45
    )

    if match:
        return answers[match[0]]

    return """
Sorry, I couldn't find an answer for your question.

You can ask questions related to:

• Password Reset
• Leave Application
• Office Timings
• IT Support

Or contact the Helpdesk Administrator.
"""