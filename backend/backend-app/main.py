from flask import Flask
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000)
