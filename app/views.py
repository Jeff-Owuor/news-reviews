from flask import render_template
from app import app
from app.request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    business_news = get_news('business')
    return render_template('index.html',business = business_news)