from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Raiders12'

@app.route('/')
def counter():
    return render_template('index.html')



@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
