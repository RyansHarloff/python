from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Show:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.description = data['description']
        self.release_date = data['release_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_show(data):
        is_valid = True
        if len(data['title']) < 3:
            flash('Title name must be 3 characters long')
            is_valid = False
        if len(data['network']) < 3:
            flash('Network name must be 3 characters long')
            is_valid = False
        if len(data['release_date']) < 3:
            flash('Release date name must be 3 characters long')
        if len(data['description']) < 3:
            flash('descirption must be 3 characters long')
        return is_valid

    @classmethod
    def save_show(cls,data):
        query = 'INSERT INTO shows(title,network, release_date, users_id, description, created_at) VALUES (%(title)s, %(network)s, %(release_date)s, %(users_id)s,%(description)s, NOW());'
        return connectToMySQL('show_exam_schema').query_db(query,data)

    @classmethod
    def all_shows(cls):
        query = 'SELECT * FROM shows'
        shows_from_db = connectToMySQL('show_exam_schema').query_db(query)
        all_shows= []
        for show in shows_from_db:
            all_shows.append(cls(show))
        return all_shows

    @classmethod
    def get_one_show(cls,data):
        query = ' SELECT * FROM shows WHERE id = %(id)s;'
        show_from_db = connectToMySQL('show_exam_schema').query_db(query,data)
        return show_from_db[0]

    @classmethod
    def update_show_info(cls,data):
        query = 'UPDATE shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s WHERE id = %(id)s;'
        updated_show = connectToMySQL('show_exam_schema').query_db(query,data)
        return updated_show

    @classmethod
    def delete_show(cls,data):
        query = 'DELETE FROM shows WHERE id = %(id)s;'
        connectToMySQL('show_exam_schema').query_db(query,data)