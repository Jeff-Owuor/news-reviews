from flask import render_template
from . import main
from app.request import get_source,get_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    usa_news_sources = get_source('us')
    britain_news_sources = get_source('gb')
    southafrica_news_sources = get_source("za")
    return render_template('index.html',usa_news = usa_news_sources,britain_news = britain_news_sources,southafrica_news= southafrica_news_sources)

@main.route('/article/<name>')
def article(name):
    article = get_article(name)
    return render_template('article.html',article_gen = article)