from flask import Flask, jsonify
from class_user import user
app = Flask(__name__)

@app.route("/")
def home():
    html_content = '''<h1>User Generating API<h1>
    <p>Go to http://127.0.0.1:5000/newusergenerate to make a new user<p>
    '''
    return html_content
@app.route("/newusergenerate")
def new_user():
    html_content = '''
    <h1>New User Generated<h1>
    '''
    u = user()
    return u.usergenerate(), html_content

if __name__ == "__main__":
    app.run()