from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, Dojos_id, created_at) VALUES (%(name)s, %(description)s, %(friend_id)s,NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
