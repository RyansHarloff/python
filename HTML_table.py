from flask import Flask, render_template
app = Flask(__name__)



@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : "Choi",'full_name': "Michael Choi"},
        {'name' : 'John', 'age' : "Supsupi", 'full_name': "John Supsupi"},
        {'name' : 'Mark', 'age' : "Guillen", 'full_name': "Mark Guillen"},
    ]
    
    return render_template("playground.html", students = student_info)




if __name__=="__main__":
    app.run(debug=True)







