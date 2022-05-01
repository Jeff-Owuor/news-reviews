from flask import render_template
from app import app
from app.request import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    usa_news_sources = get_source('us')
    britain_news_sources = get_source('gb')
    southafrica_news_sources = get_source("za")
    return render_template('index.html',usa_news = usa_news_sources,britain_news = britain_news_sources,southafrica_news= southafrica_news_sources)
