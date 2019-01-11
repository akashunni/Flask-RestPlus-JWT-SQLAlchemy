from flask_script import Manager
from flask_migrate import MigrateCommand
from the_app_api.app_file import app
from the_app_api.resources.create_db import init_db, drop_db

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(debug=True)

@manager.command
def dropdb():
    drop_db()

@manager.command
def initdb():
    init_db()

if __name__ == "__main__":
    manager.run()