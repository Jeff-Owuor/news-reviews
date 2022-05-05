
import urllib.request,json
from . import source_model,articles_model

News = source_model.News_source
Articles = articles_model.News_article

# Getting api key
api_key = None
# Getting the news sources url
base_url = None
#Getting the news articles url 
article_url = None
def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    article_url = app.config["NEWS_ARTICLE_URL"]

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format("4fd2b95bee8d40c581f5588f3a0a9c35")
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def get_article(country):
    get_articles_url = article_url.format(country,"4fd2b95bee8d40c581f5588f3a0a9c35")
    get_article_url = get_articles_url.replace(" ","-")
    with urllib.request.urlopen(get_article_url) as url:
        news_details_data = url.read()
        article_details_response = json.loads(news_details_data)
        news_object = None
        article_results_list = article_details_response['articles']
        article_results = []
        for article in article_results_list:
            description = article.get('description')
            image = article.get('urlToImage')
            date_created = article.get('publishedAt')
            link_to_article = article.get("url")
            news_object = Articles(description,image,date_created,link_to_article)
            article_results.append(news_object)
    return article_results       

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
        source_name = news_item.get('name')
        source_id = news_item.get("id")
        url = news_item.get("url")
        news_object = News(source_name,source_id,url)
        news_results.append(news_object)
    return news_results