from flask import render_template
from flask import request 
from app import app
import wiki_phil as wp


# ROUTING/VIEW FUNCTIONS
@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/author')
def author():
    # Renders author.html.
    return render_template('author.html')



@app.route('/search',methods=['POST'])
def search():
    article = request.form.get("article", None)
    path = wp.search_article(article)
    path = [term.split('_(')[0].replace('_',' ') for term in path]
    return render_template('search.html',article=article, path=path)
