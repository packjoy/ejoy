from flask_migrate import MigrateCommand
from flask_script import Manager, Server
from packjoy import create_app

app = create_app(config_filename='../config_dev.py')

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()