from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

# ! CREATE
@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    dojo_id = Dojo.save(request.form)
    return redirect('/dojos/' + str(dojo_id))

# ! READ
@app.route('/dojos')
def home():
    return render_template('index.html', dojos = Dojo.read_all())

@app.route('/dojos/<int:id>')
def show_dojo(id):
    return render_template('dojo.html', dojo = Dojo.get_dojo_with_ninjas({'id' : id}))

