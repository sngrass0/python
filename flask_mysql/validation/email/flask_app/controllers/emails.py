from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    print(request.form)
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(request.form)
    session['email'] = request.form['email']
    return redirect('/success')

@app.route('/success')
def success_page():
    return render_template('success.html', emails = Email.recent_entries())

@app.route('/delete/<int:id>')
def delete_email(id):
    Email.delete_email({'id' : id})
    return redirect('/success')





    



