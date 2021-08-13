import os

class Config:
   
    # SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}&language=en'
    # ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    # NEWS_API_KEY = 'e2ae393fb095455989ead1e0dea06939'
    
class ProdConfig(Config):
     pass
 
class DevConfig(Config):
    DEBUG = True
    
Config_options = {
    'development': DevConfig,
    'production': ProdConfig
}