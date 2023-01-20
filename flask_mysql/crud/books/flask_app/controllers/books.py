from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book
from flask_app.models import author

# ! READ MANY
@app.route('/books')
def display_books():
    return render_template('library.html', books = Book.get_all())

# ! READ ONE
@app.route('/books/<int:id>')
def display_book_info(id):
    return render_template('book.html', book = Book.get_book_with_favorites({'id' : id}), authors = author.Author.get_all())

# ! CREATE
@app.route('/books/create', methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

# ! UPDATE
@app.route('/books/favorite', methods=['POST'])
def add_favorite():
    Book.favorite(request.form)
    return redirect('/books/' + request.form['id'])