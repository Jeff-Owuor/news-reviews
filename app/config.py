class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines?country={}&apiKey={}"
    NEWS_ARTICLE_URL = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
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