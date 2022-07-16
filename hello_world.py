from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/99-bottles')
def get_bottles():
    return render_template('bottles.html', bottles=range(99, 0, -1))

