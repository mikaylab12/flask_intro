from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/index/')
def index():
    return "Welcome to my homepage"

@app.route('/about/')
def about():
    return"What would you like to know?"

if __name__ == '__main__':
    app.debug = True
    app.run()
