from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'The pipeline will automate everything!'


if __name__ == '__main__':
    app.run(debug=True)

