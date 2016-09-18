"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask
# from FlaskWebProject import app
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/requests/<request>', methods=['GET', 'POST'])
def request(request):
    return 'hello world ' + request
