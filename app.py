from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello user! This is my first flask app'

@app.route('/about')
def about():
    return 'This is about us page'

@app.route('/contact')
def contact():
    return 'This is contact us page'

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        return "You send Data!!"
    else:
        return "You are only viewing the form"