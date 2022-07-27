from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', greeting='Hello World!')


@app.route('/99-bottles')
def get_bottles():
    return render_template('bottles.html', bottles=range(99, 0, -1))


@app.route('/args/')
def args():
    return render_template(
        'args.html',
        query=request.args.lists(),
    )


@app.route('/json/')
def json_response():
    return dict(request.args.lists())


@app.route('/error')
def error():
    return 1 / 0
