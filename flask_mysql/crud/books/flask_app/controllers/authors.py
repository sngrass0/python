from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')
    
# ! READ MANY
@app.route('/authors')
def display_authors():
    return render_template('index.html', authors = Author.get_all())

# ! READ ONE
@app.route('/authors/<int:id>')
def display_author_info(id):
    return render_template('author.html', author = Author.get_author_with_favorites({'id' : id}), books = Book.get_all())

# ! CREATE
@app.route('/authors/create', methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/authors')

# ! UPDATE
@app.route('/authors/favorite', methods=['POST'])
def add_author_favorite():
    Author.favorite(request.form)
    return redirect('/authors/' + request.form['id'])