from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/recipes')
    return render_template('index.html')

# ! CREATE
@app.route("/users/register", methods = ['post'])
def register():
    print(request.form)

    #validate our user
    if not User.validate_user(request.form):
        return redirect('/')

    #hash the password
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    print(hashed_pw)

    #save the user to the database
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_pw,
    }
    user_id = User.save(data)
    #log in the user
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']

    #redirect user to app
    return redirect('/recipes')

#! READ and VERIFY AKA LOGIN
@app.route('/users/login', methods=['post'])
def login():
    print(session)
    #see of the email is in our DB
    user = User.get_by_email(request.form);
    if not user:
        flash('invalid email', 'login')
        return redirect('/')

    #check to see of the password provided matches the password in our DB
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", 'login')
        return redirect('/')

    #log in the user
    session['user_id'] = user.id
    session['first_name'] = user.first_name

    #redirect user to app
    return redirect('/recipes')

@app.route('/users/logout')
def login_user():
    session.clear()
    return redirect('/')

# ! UPDATE


# ! DELETE
