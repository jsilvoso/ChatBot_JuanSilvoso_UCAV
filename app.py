from flask import Flask, render_template
import requests
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

