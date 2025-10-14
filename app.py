from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student_profile():
    return render_template(
        "profile.html",
        name="Arun",
        is_toppe=True,
        subjects = ['Maths','Science','History']
    )