class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q={}&sortBy=publishedAt&apiKey={}'
    # NEWS_API_KEY = 'bc0e9653f5b94bb884afc47e3704ebb6'

class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True