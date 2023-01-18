from flask import Flask, render_template, redirect, request
#import the class from friend.py
from user import User

app = Flask(__name__)

# ! CREATE
@app.route('/users/new')
def new_user():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/users')

# ! READ
@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def show_all_users():
    # call the get all classmethod to get all user
    user = User.get_all()
    print(user)
    return render_template('home.html', all_users = user)


if __name__ == '__main__':
    app.run(debug=True)