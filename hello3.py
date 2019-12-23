from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index1.html', name=random.randint(0,100))
