import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', output=None)

@app.route('/calculate')
def calculate():
    amt_corn = request.form.get('amt_corn')
    quality = request.form.get('quality')
    destination = request.form.get('destiation')
    cost = request.form.get('cost')
    corn = amt_corn * (quality * .1)
    dest = destination / 1000
    if dest > 1:
        output = (cost*corn) / dest
    else:
        output = (cost*corn) / 1
    return render_template('index.html', output=output)

if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()