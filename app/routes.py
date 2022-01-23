from flask import render_template, request, jsonify, redirect
from flask.helpers import url_for
from app import app

@app.route("/")
def home_page():
    return render_template("index.html")