from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    info = {
        "instagram" : "@ebenlewis23",
        "email" : "elewis27@nmhschool.org",
        "GitHub" : "EbenLewis"
    }

    return render_template("contact.html", info=info)


@app.route("/about")
def about():
    author = "Eben Lewis"
    interests = ["Guitar","Music Production","Electrical Engineering","Computer Technology"]
    tools = ["Flask","HTML","CSS","Jinja2"]
    return render_template("about.html", author=author, interests=interests, tools=tools)

app.run(debug=True)