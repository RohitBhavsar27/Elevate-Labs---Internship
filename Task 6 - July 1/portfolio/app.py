from flask import Flask, render_template, request, redirect, url_for
from email.message import EmailMessage
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/sendemail/", methods=["POST"])
def sendemail():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["Subject"]
        email = request.form["_replyto"]
        message = request.form["message"]

        # Replace with your Gmail credentials
        your_email = "bhavsar.rohit.m@gmail.com"
        your_password = "wujb opvi jdnb koez"  # Use an App Password if 2FA is enabled

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
