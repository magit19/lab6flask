from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index3.html', name=random.randint(0,100)	)
