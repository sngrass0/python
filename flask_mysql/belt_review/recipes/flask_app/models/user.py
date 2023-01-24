# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# import a prettier print
from pprint import pprint
from flask import flash
import re
from flask_app.models import recipe
# model the class after the user table from our database
DATABASE = 'recipes_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! CREATE
    # class method to save our user to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)    
    
    # ! READ ALL
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    # ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # result returns a LIST of dictionaries
        pprint(result[0])
        # take the top dictionary and convert it into USER instance
        user = User(result[0])
        print(user)
        return user
    
    # ! UPDATE
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! DELETE
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! GET EMAIL
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) > 0:
            return User(result[0])
        else:
            return False

     # ! VALIDATE
    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True
        query = "SELECT * FROM useres WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, user)
        # validate form data
        if results and len(results) >= 1:
            is_valid = False
            flash('email is already taken', 'signup')
        if len(user['first_name']) < 2 or len(user['last_name']) < 2:
            is_valid = False
            flash('names must be more than 2 characters', 'signup')
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Invalid email address!", "signup")
        if len(user['password']) < 8:
            is_valid = False
            flash('password must be atleast 8 characters long', 'signup')
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash('passwords do not match', 'signup')

        return is_valid