from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'dojos_and_ninjas_schema'

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! READ ALL
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)

        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )

        return ninjas
    
    # ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # result returns a LIST of dictionaries
        pprint(result[0])
        # take the top dictionary and convert it into NINJA instance
        ninja = cls(result[0])
        print(ninja)
        return ninja

    # ! UPDATE
    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ! DELETE
    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)