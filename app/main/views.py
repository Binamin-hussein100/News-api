from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_article

@main.route('/', methods = ['GET'])
def index():
    
    UPDATES = get_sources()
    title = "INT NEWS"
    
    
    return render_template("index.html", UPDATES = UPDATES)
   
@main.route('/article/<id>') 
def article(id):
    
   
    Articles = get_article(id)
    title = "binamin"
    
    return render_template('articles.html', Articles = Articles)    
