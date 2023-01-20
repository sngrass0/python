from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('index.html')

#! CREATE AKA REGISTER

@app.route("/register", methods = ['post'])
def register():
    print(request.form)

    # TODO validate our user
    if not User.validate_user(request.form):
        return redirect('/')

    # TODO hash the password
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    print(hashed_pw)

    # TODO save the user to the database
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_pw,
    }
    user_id = User.save(data)
    # TODO log in the user
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']

    # TODO redirect user to app
    return redirect('/dashboard')


#! READ and VERIFY AKA LOGIN

@app.route('/login', methods=['post'])
def login():
    print(session)
    # TODO see of the email is in our DB
    user = User.get_by_email(request.form);
    if not user:
        flash('invalid email', 'login')
        return redirect('/')

    # TODO check to see of the password provided matches the password in our DB
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", 'login')
        return redirect('/')

    # TODO log in the user
    session['user_id'] = user.id
    session['first_name'] = user.first_name

    # TODO redirect user to app
    return redirect('/dashboard')
    

#! LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ! DASHBOARD
@app.route('/dashboard')
def display_dash():
    if 'user_id' not in session:
        print('User not logged in')
        return redirect('/logout')
    return render_template('home.html', user = User.get_one({'id' : session['user_id']}))