from flask import render_template
from app import main


# View
@main.route('')
def index():
    '''
    view root page fxn that returns the index page and its data
    '''
    title = 'Welcome to this awesome blog'
    return render_template('index.html', title=title)
