from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.message import Message

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login_page():
    return render_template('index.html')

# ! READ
@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/logout')
    return render_template('dashboard.html', users = User.get_users(), messages = Message.get_posts({'id' : session['user_id']}))

# ! CREATE
@app.route('/user/new', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/login')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_pw,
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    return redirect('/dashboard')

@app.route('/user/login', methods=['post'])
def login():
    print(session)
    user = User.get_by_email(request.form);
    print(user.id)
    if not user:
        flash('invalid email', 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/')

    session['user_id'] = user.id
    session['first_name'] = user.first_name

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
