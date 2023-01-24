from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models import user

DATABASE = 'wall_schema'

class Message:
    # set attributes
    def __init__(self, data):
        self.id = data['id']
        self.reciever = data['reciever']
        self.author = data['author']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! CREATE
    @classmethod 
    def save(cls, data):
        query = "INSERT INTO messages (user_id, author_id, message, created_at, updated_at) VALUES (%(user_id)s, %(author_id)s, %(message)s, NOW(), NOW())"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_posts(cls, data):
        reciever = user.User.get_users_by_id( data['id'] )
        query = """SELECT messages.*, authors.* FROM messages 
                JOIN users AS authors ON authors.id = messages.author_id 
                WHERE user_id = %(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        messages = []
        for message in results:
            author_data = {
                'id' : message['user_id'],
                'first_name' : message['first_name'],
                'last_name' : message['last_name'],
                'email' : message['email'],
                'password' : message['password'],
                'created_at' : message['authors.created_at'],
                'updated_at' : message['authors.updated_at'],
            }
            author = user.User(author_data)
            
            msg_data = {
                'id' : message['id'],
                'reciever' : reciever,
                'author' : author,
                'message' : message['message'],
                'created_at' : message['created_at'],
                'updated_at' : message['updated_at'],
            }
            messages.append( cls(msg_data) )
        return messages

    # ! DELETE
    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)



