from flask import Flask
import random


app = Flask(__name__)

@app.route('/')
def hello_world():
	a = random.random()
    return "<h1> LAB1 </h1> <p>Счастливое число:</p>"
    		
