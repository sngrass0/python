from flask import render_template, redirect, request, session, flash
from flask_app.models.message import Message
from flask_app import app

@app.route('/messages/post', methods = ['POST'])
def save_message():
    Message.save(request.form)
    return redirect('/dashboard')

@app.route('/messages/delete/<int:id>')
def delete_message(id):
    Message.delete_message({'id' : id})
    return redirect('/dashboard')