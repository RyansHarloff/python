from flask import app
from flask import render_template,redirect,request,session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/new")
def new():
    return render_template("create.html", all_dojos = Dojo.all_dojos())


@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    data = {
        " First Name":request.form['first_name'],
        "Last Name":request.form['last_name'],
        "Dojos_id":request.form['Dojos_id']
    }
    Dojo.save_dojo(data)
    return redirect('/')