from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("index.html", all_users = users)
                

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

if __name__ == "__main__":
    app.run(debug=True)
