from flask import Flask
from class_user import user
app = Flask(__name__)

@app.route("/")
def home():
    html_content = '''<h1>User Generating API<h1>'''
    return html_content
@app.route("/newusergenerate")
def new_user():
    user.usergenerate()

if __name__ == app: 
    app.run()