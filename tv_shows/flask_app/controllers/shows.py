from typing import Sized
from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.show import Show


@app.route('/add_show')
def add_show():
    if 'user_id' not in session:
        flash('Please login or register')
        return redirect('/')
    return render_template('add_show.html')

@app.route('/add_show_to_db', methods = ['POST'])
def add_show_to_db():

    if not Show.validate_show(request.form):
        return redirect('/add_show')

    data ={
        'title' : request.form['title'],
        'network' : request.form['network'],
        'release_date' : request.form['release_date'],
        'description' : request.form['description'],
        'users_id' : session['user_id']
    }

    Show.save_show(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show_info(id):
    data={
        'id' : id
    }
    show = Show.get_one_show(data)
    return render_template('show_info.html', show = show)


@app.route('/edit/<int:id>')
def edit_show(id):
    data={
        'id' : id
    }
    show = Show.get_one_show(data)
    return render_template('edit_show.html', show = show)

@app.route('/update_show/<int:id>', methods = ['POST'])
def update_show(id):
    if not Show.validate_show(request.form):
        return redirect(f'/edit_show/{{id}}')

    data = {
        'id' : id,
        'title' : request.form['title'],
        'network' : request.form['network'],
        'release_date' : request.form['release_date'],
    }
    
    Show.update_show_info(data)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete_show(id):
    data={
        'id': id
    }
    Show.delete_show(data)
    return redirect('/dashboard')