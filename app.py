from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback', methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('username') 
        message = request.form.get('message')

        return render_template('thankyou.html', user=name, message=message)
    
    return render_template("feedback.html")




@app.route('/profile')
def profile():
    return render_template(
        "profile.html",
        name="Arun",
        is_toppe=True,
        subjects = ['Maths','Science','History']
    )


@app.route('/login')
def login():
    return render_template('login.html')

