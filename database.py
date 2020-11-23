from mongoengine import connect

def init_db():
    connect('local')

