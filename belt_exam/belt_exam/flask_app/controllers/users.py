from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')

    hashed_pw = bcrypt.generate_password_hash(request.form['password'])


    data= {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_pw,
    }
    
    User.register_user(data)
    return redirect('/dashboard')