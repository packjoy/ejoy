from packjoy.common.models import *
from packjoy import db



def remove_invalid_customer_b_users():
	'''
	This is used to remove
	duplicated users and users
	with missing email addresses
	'''
	for user in User.query.all():
		if user.has_role('customer_b'):
			if not user.emails:
				db.session.delete(user)
				db.session.commit()
				print('User {} has been deleted'.format(user.name))


def create_roles():
	'''
	Creates the roles 
	for admin and scraped
	busineiss customers
	'''
	roles = [Role(name='Admin', description='Admin Role'), 
		Role(name='customer_b', description='Scraped Business Customers')]
	for role in roles:
		db.session.add(role)
	db.session.commit()


def create_super_user():
	'''
	Creates one superuser
	with all the roles
	email = szeka1994@gmail.com
	pass = gyerebe123
	'''
	user=User(password='gyerebe123', active=True,
			email='szeka1994@gmail.com', emails=['szeka1994@gmail.com'],
			roles=Role.query.all())
	db.session.add(user)
	db.session.commit()


def update_postgress_with_cutomer_b():
	for user in User.query.all():
		print(user)





if __name__ == '__main__':
	update_postgress_with_cutomer_b()