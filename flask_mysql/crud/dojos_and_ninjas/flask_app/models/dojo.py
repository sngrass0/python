from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
from pprint import pprint

DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)   

    # ! READ ALL
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)

        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )

        return dojos

    # ! READ ALL
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # result returns a LIST of dictionaries
        pprint(result[0])
        # take the top dictionary and convert it into USER instance
        dojo = cls(result[0])
        print(dojo)
        return dojo

    # ! READ RELATIONSHIPS
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls( results[0] )
        for row in results:
            ninja_data = {
                "id" : row['ninjas.id'],
                "dojo_id" : row['dojo_id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "created_at" : row['ninjas.created_at'],
                "updated_at" : row['ninjas.updated_at']
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )
        return dojo

    # ! UPDATE
    @classmethod
    def update_dojo(cls, data):
        query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)