# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# import a prettier print
from pprint import pprint
import re
from flask_app import flash
# model the class after the dojo table from our database
DATABASE = 'email_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! CREATE
    # class method to save our dojo to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails ( email, created_at, updated_at) VALUES ( %(email)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)  

    # ! READ 
    @classmethod
    def recent_entries(cls): 
        query = "SELECT * FROM emails"
        results = connectToMySQL(DATABASE).query_db(query)

        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails

    # ! DELETE
    @classmethod
    def delete_email(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! VALIDATE USER 
    @staticmethod
    def validate_email(email:dict) -> bool:
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.", "email")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!", "email")
            is_valid = False

        return is_valid

    