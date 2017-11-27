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



def update_postgress_with_cutomer_b():
	for user in User.query.all():
		print(user)





if __name__ == '__main__':
	update_postgress_with_cutomer_b()