from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("Home.html")


@app.route("/contacts")
def contacts():
    return render_template("Contacts.html")


@app.route("/projects")
def projects():
    return render_template("Projects.html")


app.run(debug=True)



