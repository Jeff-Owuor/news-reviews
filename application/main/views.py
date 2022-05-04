from flask import render_template
from . import main
from application.request import get_source,get_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    all_sources = get_source()
    return render_template('index.html',all_sources = all_sources)

@main.route('/article/<id>')
def article(id):
    article = get_article(id)
    return render_template('article.html',article_gen = article)