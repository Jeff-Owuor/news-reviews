from cmath import pi
from app import app
import urllib.request,json
from .models import news

News = news.News_source
Articles = news.News_article

# Getting api key
api_key = app.config['NEWS_API_KEY']
#Getting the base url
base_url = app.config["NEWS_BASE_URL"]

article_url = app.config["NEWS_ARTICLE_URL"]

def get_source(country):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(country,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def get_article(source_name):
    get_articles_url = article_url.format(source_name,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        news_details_data = url.read()
        article_details_response = json.loads(news_details_data)

        news_object = None
        if article_details_response:
            description = article_details_response.get('description')
            image = article_details_response.get('urlToImage')
            date_created = article_details_response.get('publishedAt')
            
            news_object = Articles(description,image,date_created)
            
    return news_object        

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        content = news_item.get("content")
        image = news_item.get("urlToImage")
        description = news_item.get("description")
        date_of_creation = news_item.get('publishedAt')
        if content:
            news_object = News(source,content)
            articles_object = Articles(image,description,date_of_creation)
            news_results.append(news_object)

    return news_results