from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
from flask_app.models.show import Show
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
    
    user_id = User.register_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    data = {
        'id' : session['user_id']
    }
    all_shows = Show.all_shows()
    user_in_session = User.one_user(data)
    return render_template('dashboard.html', user = user_in_session, shows = all_shows)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')