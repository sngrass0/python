# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# import a prettier print
from pprint import pprint
import re
from flask_app import flash
# model the class after the user table from our database
DATABASE = 'login_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
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
        user = cls(result[0])
        print(user)
        return user

    # ! UPDATE
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! DELETE
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    
    # TODO Write a query method to verify the email entered in the login form
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) > 0:
            return User(result[0])
        else:
            return False
    
    # ! VALIDATE USER 
    @staticmethod
    def validate_user(user:dict) -> bool:
        is_valid = True
        
        if len(user['first_name']) < 2:
            is_valid = False
            flash('invalid name input', 'register')
        if not re.search(r'\d', user['password']):
            is_valid = False
            flash('password must contain atleast one digit', 'register')
        if not re.search(r'[ A-Z]', user['password']):
            is_valid = False
            flash('password must contain atleast one Uppercase', 'register')
        if user['password'] != user['confirm-password']:
            is_valid = False
            flash('passwords do not match', 'register')
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash('invalid email', 'register')
        if len(user['password']) < 8:
            is_valid = False
            flash('password must be at least 8 characters', 'register')


        return is_valid