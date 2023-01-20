from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models import author

DATABASE = 'books_schema'

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []
    
    # ! CREATE
    # class method to save our book to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books ( title, num_of_pages, created_at, updated_at) VALUES ( %(title)s, %(num_of_pages)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)   

    @classmethod
    def favorite(cls, data):
        query ="INSERT INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(id)s);"
        return connectToMySQL(DATABASE).query_db(query, data) 
    
    # ! READ ALL
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of books
        books = []
        # Iterate over the db results and create instances of books with cls.
        for book in results:
            books.append( cls(book) )
        return books
    
    # ! READ ONE
    @classmethod
    def get_book_with_favorites(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.user_id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # get first and story instance
        book = cls(results[0])
        for row in results:
            fav_data = {
                'id' : row['authors.id'],
                'name' : row['name'],
                'created_at' : row['authors.created_at'],
                'updated_at' : row['authors.updated_at'],
            }
            book.favorites.append( author.Author(fav_data) )
        return book

    # ! UPDATE
    @classmethod
    def update_book(cls, data):
        query = "UPDATE books SET title = %(title)s, num_of_pages = %(num_of_pages)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! DELETE
    @classmethod
    def delete_book(cls, data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)