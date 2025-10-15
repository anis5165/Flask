from flask import Flask, render_template, request, flash, redirect, url_for
from form import RegistrationForm

app = Flask(__name__)
app.secret_key = 'mainhoonna'

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/register", methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome, {name}! You Registered Successfully", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")



#flash messages
@app.route('/feedback', methods=['POST','GET'])
def feedback():
    if request.method == 'POST':
        name = request.form.get("username")
        if not name:
            flash("Name cannot be empty")
            return redirect(url_for("feedback"))
        flash(f"Thanks {name}, your feedback was saved")
        return redirect(url_for("thankyou"))
    return render_template("feedback.html")


@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")


# @app.route('/feedback', methods=['GET','POST'])
# def feedback():
#     if request.method == 'POST':
#         name = request.form.get('username') 
#         message = request.form.get('message')

#         return render_template('thankyou.html', user=name, message=message)
    
#     return render_template("feedback.html")




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

