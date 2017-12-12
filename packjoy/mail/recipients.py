from packjoy.common.models import User


class Recipients(object):
	def __init__(self, filters, users):
		if users is not None:
			self.users = users
		else:
			self.users = self.get_users_by_filters(filters, users)
	

	@staticmethod
	def get_users_by_filters(filters, emails):		
		if 'every_user' in filters:
			return User.query.all()
