from flask_app import app
from flask_app.controllers import users
from flask_app.models.user import user
from flask import render_template,redirect,request,session,flash
from mysqlconnection import connectToMySQL
@app.route("/")
def index():
    return render_template("index.html", all_users = user.get_all_users())
                

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at)VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(),NOW());"

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"],
    }
    db = connectToMySQL("users_schema")
    db.query_db(query,data)
    return redirect('/')

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/show/<id>")
def show(id):
    data={
        "id":int(id)
    }
    return render_template('show.html', user = User.one_user(data))

@app.route("/delete/<id>")
def delete(id):
    query = "DELETE FROM users WHERE id = %(id)s"
    data={
        "id":int(id)
    }
    mysql = connectToMySQL("users_schema")
    mysql.query_db(query,data)
    return redirect('/')

@app.route("/edit/<id>")
def edit(id):
    query = "SELECT * FROM users WHERE id = %(id)s"
    data={
        "id":int(id)
    }
    mysql = connectToMySQL("users_schema")
    user = mysql.query_db(query,data)
    return render_template('edit.html', user = user[0])

@app.route('/update/<id>', methods=["POST"])
def update(id):
    query = "UPDATE users SET first_name = %(first_name)s, last_name=%(last_name)s, email = %(email)s WHERE id = %(id)s;"
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': int(id)
    }
    mysql = connectToMySQL("users_schema")
    mysql.query_db(query,data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
