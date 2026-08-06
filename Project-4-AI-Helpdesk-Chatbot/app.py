from flask import Flask, render_template, request, redirect
import sqlite3
from chatbot import get_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":
        question = request.form["question"]
        reply = get_response(question)

    return render_template("index.html", reply=reply)


@app.route("/admin", methods=["GET", "POST"])
def admin():

    conn = sqlite3.connect("helpdesk.db")
    cursor = conn.cursor()

    if request.method == "POST":

        question = request.form["question"]
        answer = request.form["answer"]

        cursor.execute(
            "INSERT INTO faq(question, answer) VALUES (?, ?)",
            (question, answer)
        )

        conn.commit()

    cursor.execute("SELECT * FROM faq")

    data = cursor.fetchall()

    conn.close()

    return render_template("admin.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
    