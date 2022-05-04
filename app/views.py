from flask import render_template,url_for
from app import app
from .request import get_news

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    trending_news = get_news('trending')
    love_news = get_news('love')
    # print(trending_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,trending = trending_news,love = love_news)


@app.route('/sports')
def sports():
    '''
    View root page function that returns the index page and its data
    '''

    sport_news = get_news('sports')
    entertain_news = get_news('entertainment')
    title = "Sports - Sports news"
    # print(trending_news)
    title = 'Welcome to The best News review  Website Online'
    return render_template('sports.html', title = title,sports=sport_news,entertainment=entertain_news)

@app.route('/politics')
def politics():
    '''
    View root page function that returns the index page and its data
    '''

    political_news = get_news('politics')
    title = "Politics - Politics news"
    # print(trending_news)
    # title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('politics.html', title = title,politics=political_news)
# if

@app.route('/technology')
def technology():
    '''
    View root page function that returns the index page and its data
    '''

    technology_news = get_news('technology')
    title = "Politics - Politics news"
    # print(trending_news)
    title = 'TechNews - Technology news'
    return render_template('technology.html', title = title,technology=technology_news)