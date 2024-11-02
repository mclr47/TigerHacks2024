import datetime
from flask import Flask, render_template
from flask_moment import Moment


app = Flask(__name__)

#----Martian
moment = Moment(app)

{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}

#in the index.html:
#<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
#<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>

#@app.route('/')
#def index():
#    return render_template('index.html',
#                           current_time=datetime.utcnow())
#---end Martian

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
