from flask import Flask
from first_package import test

app = Flask(__name__)


# Testing
@app.route('/')
def hello_world():
    return test()

@app.test('/test')
def test():
    return test()


if __name__ == '__main__':
    app.run()