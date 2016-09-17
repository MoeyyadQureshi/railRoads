"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    
    
@app.route('/awesome')
def awesome():
    """Renders awesome"""
    return render_template(
        'awesome.html',
        title='AWESOME',
    )