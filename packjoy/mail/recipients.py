from packjoy.common.models import User


class Recipients(object):
	def __init__(self, filters):
		self.users = self.get_users_by_filters(filters)

	@staticmethod
	def get_users_by_filters(filters=[]):
		if 'send_to_every_user' in filters:
			return User.query.all()