from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    print(request.form)
    if not Dojo.validate_user(request.form):
        return redirect('/')
    Dojo.save(request.form)
    return redirect('/user')

@app.route('/user')
def display_results():
    return render_template('user.html', survey = Dojo.get_last_survey())





    



