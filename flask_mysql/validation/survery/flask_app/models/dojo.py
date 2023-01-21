# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# import a prettier print
from pprint import pprint
import re
from flask_app import flash
# model the class after the dojo table from our database
DATABASE = 'dojo_survey_schema'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! CREATE
    # class method to save our dojo to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, location, language, comment, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)    
    
    @classmethod 
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1"
        results = connectToMySQL(DATABASE).query_db(query)
        return cls(results[0])
    
    # ! VALIDATE USER 
    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True
        if len(user['name']) < 2:
            is_valid = False
            flash('invalid name input', 'register')
        if user['location'] == '--Select A Location--':
            is_valid = False
            print(user['location'] )
            flash('Must choose a location field', 'register')
        if user['language'] == '--Select A Language--':
            is_valid = False
            flash('Must choose a language field', 'register')
        if len(user['comment']) < 3:
            is_valid = False
            flash('Comments must be atleast 3 characters long', 'register')

        return is_valid