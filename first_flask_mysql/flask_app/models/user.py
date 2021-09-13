#from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name=data['first_name']
        self.last_name = data['last_namae']
        self.email = data['email']
        self.creeated_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def get_all_users(cls):
    query = 'SELECT * FROM friends;'
    users_from_db = connectToMySQL('users.schema').query_db(query)

    all_users = []
    for user in users_from_db:
        all_users.append(cls(user))
    return all_users

@classmethod
def one_user(cls, data):
    query = "SELECT * FROM users WHERE id = %(data['id']))s"
    only_user = connectToMySQL('users_schema').query_db(query)

    return cls(only_user[0])