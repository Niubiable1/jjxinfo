from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET, POST"])
def index():
  return render_template("index.html")