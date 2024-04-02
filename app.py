from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] ='secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    return render_template('home.html', survey = satisfaction_survey)

@app.route('/questions/<int:num>')
def show_question(num):
    if(num != len(responses)):
        flash("Attempting to access invalid question. Redirecting...")
        return redirect(f"/questions/{len(responses)}")
    if(len(responses) == len(satisfaction_survey.questions)):
        return redirect("/complete")
    return render_template('questions.html', question = satisfaction_survey.questions[num])

@app.route('/answer', methods=["POST"])
def store_answer():
    choice = request.form['answer']
    responses.append(choice);
    return redirect(f'/questions/{len(responses)}')

@app.route('/complete')
def complete():
    return render_template("complete.html")