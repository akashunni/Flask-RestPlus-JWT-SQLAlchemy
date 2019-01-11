# from the_app_api.app_file import db
from the_app_api.resources.base import db
from the_app_api.resources import models

def drop_db():
    db.reflect()
    db.drop_all()
    print("DROP DB DONE...")

def init_db():
    drop_db()
    db.create_all()
    db.session.add(models.User(username='akashadmin', password='password', role='admin'))
    db.session.add(models.User(username='akashend', password='password', role='enduser'))
    db.session.commit()
    print("Init DB done...")

