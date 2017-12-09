from packjoy.common.models import *
from packjoy import create_app
from packjoy.common.models import db


app = create_app('../config_prod.py')


def save_to_prod_db(users=None):
	app = create_app('../config_dev.py')
	app.config.update(
		DEBUG=False,
		SECRET_KEY='saidnuhqiodjqwijxqwuihyggggqwijqwihdiqw',
		SQLALCHEMY_DATABASE_URI='postgres://cmtfafkbphxvov:be9192275b221161b9dbcabe3a067ead13c1287d45d07698a90e848fe9301409@ec2-54-247-187-134.eu-west-1.compute.amazonaws.com:5432/dac4l0v90g0o9u'
	)
	with app.app_context():
		customer_b = Role.query.filter_by(name='customer_b').first()
		print(customer_b)
		for u in users:
			# if User.query.filter_by(email=u.email).count() > 0:
			# 	print('This is already in the database')
			# 	continue
			user = User(roles=[customer_b], active=True,
					email=u.email, name=u.name,
					emails=[Email(email=str(e)) for e in u.emails])
			db.session.add(user)
			db.session.commit()	
			print('Adding: {}'.format(user.email))
			


		# for user in users:
		# 	if user.email is None and len(user.emails) > 0:
		# 		user.email = str(user.emails[0])
		# 	# if User.query.filter_by(email=user.email).first() is None:
		print(User.query.all())		


def remove_invalid_customer_b_users():
	'''
	This is used to remove
	duplicated users and users
	with missing email addresses
	'''
	with app.app_context():
		for user in User.query.all():
			if user.has_role('customer_b'):
				if not user.emails:
					db.session.delete(user)
					db.session.commit()
					print('User {} has been deleted'.format(user.name))
		for email in Email.query.all():
			if email.user is None:
				db.session.delete(email)
				db.session.commit()
				print('{} has no user'.format(email))



def update_postgress_with_cutomer_b():
	with app.app_context():
		users = User.query.all()
		save_to_prod_db(users)

if __name__ == '__main__':
	remove_invalid_customer_b_users()