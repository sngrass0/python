from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
import re
from flask import flash
from flask_app.models import message

DATABASE = 'wall_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    # initialize values
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # ! CREATE
    @classmethod 
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! READ
    @classmethod
    def get_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_users_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results < 1:
            return False
        return cls( results[0] )

    
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
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, user)
        # validate form data
        if len(result) > 1:
            is_valid = False
            flash('email already exists', 'signup')
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