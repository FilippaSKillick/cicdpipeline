from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello universe I have the best husband!'


if __name__ == '__main__':
    app.run(debug=True)

