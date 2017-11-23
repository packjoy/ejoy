from flask_migrate import MigrateCommand
from flask_script import Manager, Server, Shell, Command, Option
from packjoy import create_app
from packjoy.common import models
from packjoy.common.models import db

app = create_app(config_filename='../config_dev.py')


class SendEmail(Command):
	'''
	This is the CLI tool to send
	different emails (based on campaign)
	to the provided email address
	'''		

	def run(self, email, campaign_type):
		pass




class CreateSuperUser(Command):
	'''
	Takes in the email and password
	and creates a new admin which 
	will have all the roles
	'''

	option_list = (
		Option('-e', '--email', dest='email'),
		Option('-p', '--password', dest='password')
	)

	def run(self, email, password):
		'''
		Need to use the utils from the
		dev branch here and print some
		success message
		'''
		print('Super User Created!')
		print('Email: {}, Password: {}'.format(email, password))


def make_context():
	return dict(app=app, db=db, models=models)




manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_context))
manager.add_command('createsuperuser', CreateSuperUser())

if __name__ == '__main__':
    manager.run()