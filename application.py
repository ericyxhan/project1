from flask import Flask, redirect, render_template, session, url_for
"""cool"""
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about.html")
def about():
    return render_template("about.html")
@app.route("/pictures.html")
def pictures():
    return render_template("pictures.html")
@app.route("/updates.html")
def updates():
    return render_template("updates.html")
