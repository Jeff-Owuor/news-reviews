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
    headlines_from_us = get_article("us")
    headlines_from_sa = get_article("sa")
    return render_template('index.html',all_sources = all_sources,headlines_from_us = headlines_from_us,headlines_from_sa = headlines_from_sa)