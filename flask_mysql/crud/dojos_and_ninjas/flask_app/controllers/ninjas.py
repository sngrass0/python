from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app.controllers import dojos

# ! CREATE
@app.route('/ninjas/new')
def ninja_form():
    return render_template('new.html', dojos = Dojo.read_all())

@app.route('/ninjas/create', methods=['POST'])
def ninja_create():
    Ninja.save(request.form)
    return redirect('/dojos/' + request.form['dojo_id'])