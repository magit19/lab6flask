from flask import Flask
import random
app = Flask(__name__)
#a = random.random() * 100
a=random.randint(1,99)
@app.route('/')
def hello_world():
    return f'<h1>Hello world!</h1><p>Поротов</p><p>Случайное число:{a}</p>'
