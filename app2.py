from flask import Flask

app2 = Flask(__name__)

@app2.route('/')
def home_page():
    return "Welcome to my page!"

@app2.route('/about_me/')
def about_me():
    return "My name is Mikayla Beelders."

@app2.route('/hobbies/')
def hobbies():
    return "I enjoy outdoor activities."

@app2.route('/contact/')
def contact():
    return "Please do not hesitate to contact me."

if __name__ == '__main__':
    app2.debug = True
    app2.run()
