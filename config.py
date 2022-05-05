import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"
    NEWS_ARTICLE_URL = "https://newsapi.org/v2/top-headlines?country={}&apiKey=4fd2b95bee8d40c581f5588f3a0a9c35"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
