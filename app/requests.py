import urllib.request,json
from .models import Sources,Article


api_key = None
source_base_url = None
article_base_url = None

def configure_request(app):
    global api_key,source_base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    source_base_url = app.config['SOURCE_BASE_URL']
    article_base_url = app.config['ARTICLES_BASE_URL']
    
def get_sources():
    url_for_sources = source_base_url.format(api_key)
    
    with urllib.request.urlopen(url_for_sources) as data:
        sources_data = data.read()
        sources_response = json.loads(sources_data)
        
        sources_results = None
        
        if sources_response['sources']:
            sources_results_list = sources_response['sources']
            sources_results = process_source_results(sources_results_list)
    return sources_results
def process_source_results(sources_list):
    
    sources_results = []
    for news_source in sources_list:
        source_name = news_source.get('name')
        source_id = news_source.get('id')
        source_url = news_source.get('url')
        source_category = news_source.get('category')
        
        source_object = Sources(source_name,source_category,source_url,source_id)
        sources_results.append(source_object)
        
    return sources_results

def get_article(source):
    
    get_article_url = article_base_url.format(source,api_key)
    print(get_article_url)
    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)
        
        articles_results = None
        
        if article_response['articles']:
            articles_results_list = article_response['articles']
            articles_results = process_article(articles_results_list)
    return articles_results
def process_article(articles_list):

        articles_results = []
        for articles in articles_list:
            author = articles.get('author')
            title = articles.get('title')
            description = articles.get('description')
            url = articles.get('url')
            urlToImage = articles.get('urlToImage')
            publish = articles.get('publishedAt')
            content = articles.get('content')
           
            article_object = Article(author,title,description,url,urlToImage,publish,content)
            articles_results.append(article_object)
         
        return articles_results
                
                
                