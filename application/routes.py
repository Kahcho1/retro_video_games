from application import app, db
from flask import render_template, request, redirect, url_for, jsonify
from application.models import Games, Console
import requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title="Home Page")