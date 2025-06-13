from flask import Flask, request, render_template, redirect, url_for
from markupsafe import Markup
import os

app = Flask(__name__)
app.jinja_env.globals["Markup"] = Markup

with open("flags/challenge1.txt") as f1, open("flags/challenge2.txt") as f2:
    FLAG1 = f1.read().strip()
    FLAG2 = f2.read().strip()

exfiltrated = []

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    query1 = request.args.get("input_user", "")
    query2 = request.args.get("input_pass", "")
    return render_template("challenge1.html", user_input1=query1, user_input2=query2, flag=FLAG1)
