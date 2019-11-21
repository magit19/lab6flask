from flask import Flask
import random
app = Flask(__name__)
a=random.randint(1,99)
@app.route('/')
def hello_world():
    return f'<h1>Hello world!</h1><p>Случайное число:{a}</p>'
