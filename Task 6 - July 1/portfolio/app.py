from flask import Flask, render_template, request, redirect, url_for
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

env = load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    project_list = [
        {
            "title": "ShareSphere - Document Sharing DApp",
            "description": "A decentralized document-sharing app built with React, IPFS, and MetaMask integration. Secure upload, access control, and blockchain-based authentication.",
            "image": "images/sharesphere.png",
            "link": "https://rohitbhavsar27.github.io/Blockchain_Document_Sharing/",
        },
        {
            "title": "E-Book Store App",
            "description": "A full-stack Angular + Django REST app with Firebase authentication. Enables browsing, searching, ordering books and includes an admin dashboard.",
            "image": "images/ebook.png",
            "link": "https://book-store-client-sable.vercel.app/",
        },
        {
            "title": "Gemini Clone - AI Chat UI",
            "description": "Built a front-end clone of Google's Gemini AI interface using modern HTML, CSS, and JavaScript. Features a responsive layout, intuitive design, and theme toggle for light/dark modes.",
            "image": "images/gemini_clone.png",
            "link": "https://rohitbhavsar27.github.io/gemini-clone/",
        },
        {
            "title": "TextUtils - Text Manipulation Tool",
            "description": "A web-based utility built with HTML, CSS, and JS to transform, analyze, and clean up text. Includes word count, case conversion, and formatting tools.",
            "image": "images/textutils.png",
            "link": "https://rohitbhavsar27.github.io/TextUtils/",
        },
        {
            "title": "Online Exam System",
            "description": "Built a full-stack system with Angular and Django REST APIs for user authentication and result management. Admin dashboard supports secure CRUD operations for questions with structured API responses.",
            "image": "images/quizly.png",
            "link": "https://online-exam-client.vercel.app/",
        },
        {
            "title": "TopicTrek - Quiz Application",
            "description": "Developed a web-based quiz application featuring diverse question types and formats. Designed to provide a dynamic and interactive user experience.",
            "image": "images/topictrek.png",
            "link": "https://rohitbhavsar27.github.io/TopicTrek-quizApp/",
        },
    ]
    return render_template("projects.html", projects=project_list)


@app.route("/sendemail/", methods=["POST"])
def sendemail():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["Subject"]
        email = request.form["_replyto"]
        message = request.form["message"]

        your_email = os.getenv("GMAIL_USER")
        your_password = os.getenv("GMAIL_PASSWORD")

        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(your_email, your_password)

        # Compose the email
        msg = EmailMessage()
        msg.set_content(
            f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        )
        msg["To"] = your_email  # Send the email to yourself
        msg["From"] = your_email
        msg["Subject"] = subject

        # Send the email
        try:
            server.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

        server.quit()
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
