from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from markupsafe import Markup
import os
import pathlib

app = Flask(__name__)
app.jinja_env.globals["Markup"] = Markup

BASE_DIR = pathlib.Path(__file__).parent
CREDS_DIR = BASE_DIR / "credentials"

@app.route("/creds/<path:filename>")
def creds(filename):
    # e.g. /creds/pass.txt
    return send_from_directory(CREDS_DIR, filename)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    query1 = request.args.get("input_user", "")
    query2 = request.args.get("input_pass", "")
    return render_template("challenge1.html", user_input1=query1, user_input2=query2)
