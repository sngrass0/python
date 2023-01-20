from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models import book

DATABASE = 'books_schema'

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    # ! CREATE
    # class method to save our author to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors ( name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data) 

    @classmethod
    def favorite(cls, data):
        query ="INSERT INTO favorites (user_id, book_id) VALUES (%(id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! READ ALL
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of authors
        authors = []
        # Iterate over the db results and create instances of authors with cls.
        for author in results:
            authors.append( cls(author) )
        return authors
    
    # ! READ ONE
    @classmethod
    def get_author_with_favorites(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.user_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # get first and story instance
        author = cls(results[0])
        for row in results:
            fav_data = {
                'id' : row['books.id'],
                'title' : row['title'],
                'num_of_pages' : row['num_of_pages'],
                'created_at' : row['books.created_at'],
                'updated_at' : row['books.updated_at'],
            }
            author.favorites.append( book.Book(fav_data) )
        return author

    # ! UPDATE
    @classmethod
    def update_author(cls, data):
        query = "UPDATE authors SET name = %(name)s, first_name = %(first_name)s, last_name = %(last_name)s, WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! DELETE
    @classmethod
    def delete_author(cls, data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)