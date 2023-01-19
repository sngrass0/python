from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

# ! CREATE
@app.route('/users/new')
def new_user():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    user_id = User.save(request.form)
    return redirect('/users/' + str(user_id))

# ! READ ALL
@app.route('/users')
def show_all_users():
    # call the get all classmethod to get all user
    user = User.get_all()
    return render_template('home.html', all_users = user)

# ! READ ALL
@app.route('/users/<int:id>')
def show_one_user(id):
    return render_template('user.html', user = User.get_one({'id' : id}))

# ! UPDATE
@app.route('/users/edit/<int:id>')
def edit_user(id):
    return render_template('edit.html', user = User.get_one({'id' : id}))

@app.route('/users/update', methods=['POST'])
def update_user():
    User.update_user(request.form)
    return redirect('/users/' + request.form['id'])

# ! DELETE
@app.route('/users/delete/<int:id>')
def delete_user(id):
    User.delete_user({'id' : id})
    return redirect('/users')