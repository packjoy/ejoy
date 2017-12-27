from packjoy.common.models import User


class Recipients(object):
	def __init__(self, filters, users):
		if users is not None:
			self.users = users
		else:
			self.users = self.get_users_by_filters(filters)
		self.recipient_variables = self.get_recipient_variables()
	

	@staticmethod
	def get_users_by_filters(filters):
		'''
		This function will get the users based on
		the passed filters
		'''
		if 'every_user' in filters:
			return User.query.all()

	def get_recipient_variables(self):
		'''
		This is the function to collect
		the different recipient variables 
		for mailgun and peronalized
		emails.
		'''
		return [{user.email: {'email': user.email}} for user in self.users]