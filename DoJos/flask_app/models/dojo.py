from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask import app

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # @staticmethod
    # def validate_friend(data): 
    #     is_valid = True # we assume this is true
    #     if len(data['fname']) < 2:
    #         flash("First name must be at least 2 characters!")
    #         is_valid = False
    #     if not NAME_REGEX.match(data['fname']):
    #         flash("First name must only contain letters!")
    #         is_valid = False
    #     if len(data['lname']) < 2:
    #         flash("Last name must be at least 2 characters!")
    #         is_valid = False
    #     if len(data['occ']) < 1: 
    #         flash("Occupation must be present!")
    #         is_valid = False
    #     if len(data['occ']) < 5:
    #         flash("Occupation must be at least 5 characters!")
    #         is_valid = False
    #     if not EMAIL_REGEX.match(data['occ']):
    #         flash("Occupation must be a valid format! Format it like an email and see!")
    #         is_valid = False
    #     return is_valid


    @classmethod
    def get_ninjas_by_dojo(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        group = cls(results[0])

        for row_from_db in results:
            data = {
                "id":row_from_db['ninjas.id'],
                "name":row_from_db['ninjas.name'],
                "created_at":row_from_db['ninjas.created_at'],
                "updated_at":row_from_db['ninjas.updated_at'],
            }
            group.ninjas.append(Ninja(data))
        return group


    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_friends = []
        for dojo in dojos_from_db:
            all_dojos.append(cls(dojo))
        return all_dojos


    @classmethod
    def one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        only_dojo = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(only_dojo[0])


    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name VALUES (%(name)s,"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)


    @classmethod
    def update_dojo(cls, data):
        query = "UPDATE dojos SET name=%(name)s WHERE id=%(id)s;"
        updated_dojo = connectToMySQL('dojos_and_ninjass_schema').query_db(query, data)
        return updated_dojo

    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)