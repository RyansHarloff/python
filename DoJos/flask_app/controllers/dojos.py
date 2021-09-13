from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html", all_dojos = Dojo.all_dojos())


@app.route("/show/<int:id>")
def show(id):
    data = {
        "id" : id
    }
    return render_template("show.html", dojo = Dojo.get_ninja_by_dojos(data))


@app.route("/create")
def create():
    return render_template("create.html")


@app.route("/create_ninja", methods=["POST"])
def create_dojo():


    data = {
        "first_name":request.form['fisrt_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age']
    }
    Dojo.save(data)
    return redirect('/')


@app.route("/delete/<id>")
def delete_dojo(id):
    data = {
        "id" : int(id)
    }
    Ninja.delete_dojo(data)
    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id" : int(id)
    }
    return render_template("edit.html", dojo = Dojo.one_dojo(data))


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "id" : id
    }
    Dojo.update_dojo(data)
    return redirect(f"/show/{id}")