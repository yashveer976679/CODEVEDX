import sqlite3
conn = sqlite3.connect("helpdesk.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

cursor.execute("SELECT COUNT(*) FROM faq")

count = cursor.fetchone()[0]

if count == 0:

    faqs = [

        ("How do I reset my password?",
         "Click on 'Forgot Password' on the login page."),

        ("How do I apply for leave?",
         "Apply through the HR Portal."),

        ("What are office timings?",
         "Office timings are 9 AM to 6 PM."),

        ("Who should I contact for IT support?",
         "Contact the IT Helpdesk at extension 101."),

        ("Laptop is not working",
         "Please raise an IT support ticket.")
    ]

    cursor.executemany(
        "INSERT INTO faq(question, answer) VALUES (?, ?)",
        faqs
    )

conn.commit()

conn.close()

print("Database Created Successfully!")