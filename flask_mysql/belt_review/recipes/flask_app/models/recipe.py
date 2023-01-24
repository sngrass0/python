# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# import a prettier print
from pprint import pprint
from flask import flash
import re
# model the class after the user table from our database
DATABASE = 'recipes_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.under = data['under']
        self.instructions = data['instructions']
        self.description = data['description']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.author = data['first_name']

        # ! CREATE
    # class method to save our user to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes ( user_id, name, under, instructions, description, date_made, created_at, updated_at) VALUES ( %(user_id)s, %(name)s, %(under)s, %(instructions)s, %(description)s, %(date_made)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)    
    
    # ! READ ALL
    @classmethod
    def get_all_user_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id ORDER BY recipes.created_at DESC;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    
    # ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # result returns a LIST of dictionaries
        pprint(result[0])
        # take the top dictionary and convert it into RECIPE instance
        recipe = cls(result[0])
        print(recipe)
        return recipe

    # ! UPDATE
    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, under = %(under)s, instructions = %(instructions)s, description = %(description)s, date_made = %(date_made)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! DELETE
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! VALIDATE
    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True

        if len(recipe['name']) < 3 or len(recipe['description']) < 3 or len(recipe['instructions']) < 3:
            is_valid = False
            flash('entries must be more than 3 characers', 'recipe')
        if recipe['date_made'] == '':
            is_valid = False
            flash('date field cannot be empty', 'recipe')

        return is_valid