from flask import Flask, request, redirect, url_for, session, Response, render_template

app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return 'This is about us page'

@app.route('/contact')
def contact():
    return 'This is contact us page'

@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/submit", methods=['POST'])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "anis5165" and password == "pass":
    #     return render_template("home.html", name= username)

    valid_users = {
        'admin':'123',
        'anis5165':'pass',
        'rajat':'raj',
        'vikas':"5165"
    }
    if username in valid_users and password in valid_users[username]:
        return render_template("home.html", name=username)

    else:
        return "Invalid credentials"









# @app.route('/submit', methods=['GET','POST'])
# def submit():
#     if request.method == 'POST':
#         return "You send Data!!"
#     else:
#         return "You are only viewing the form"

#login page
# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')

#         if username == 'admin' and password == '123':
#             session['user'] = username #store in session
#             return redirect(url_for('welcome'))
#         else:
#             return Response("Invalid Credentials. Try Again", mimetype='text/plain')
#     return '''
#         <h2>Login Form </h2>
#         <form method='POST'>
#             Username: <input type='text' name='username'><br>
#             Password: <input type='text' name='password'><br>
#             <input type="submit" value="login">
#         </form>
#     '''


# #welcome page after login
# @app.route('/welcome')
# def welcome():
#     if "user" in session:
#         return f'''
#         <h2> Welcome, {session["user"]}!!</h2>
#         <a href={url_for("logout")}>Logout</a>
#     '''
#     return redirect(url_for("login"))

# #logout function
# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect(url_for("login"))
    
    