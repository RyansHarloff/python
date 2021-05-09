from flask import Flask, render_template
app = Flask(__name__)



@app.route('/play')
def bluebox():
    return render_template('playground.html', times=3)


@app.route('/play/<int:x>')
def second(x):
    return render_template('playground.html', times=x)



if __name__=="__main__":
    app.run(debug=True)







