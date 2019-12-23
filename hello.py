from flask import Flask
import random

app = Flask(__name__)
a = random.random() * 100
@app.route('/')
def hello_world():
    return f"<h1> LAB1 </h1> <p>Случайное число: {a}</p>"
    		
