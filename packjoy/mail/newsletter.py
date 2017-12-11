from .campaigns import PriceDecrease, BackInStock, Welcome, NewArrivals
from .recipients import Recipients


class Newsletter(object):
	def __init__(self, filters=[], campaign_type=None):
		self.recipients = Recipients(filters)
		if campaign_type == 'price_decrease':
			self.campaign = PriceDecrease()
		elif campaign_type == 'back_in_stock':
			self.campaign = BackInStock()
		elif campaign_type == 'welcome':
			self.campaign = Welcome()
		elif campaign_type == 'new_arrivals':
			self.campaign = NewArrivals()
		else:
			raise NotImplementedError('campaign_type: {} is not implemented yet'.format(campaign_type))



	@staticmethod
	def send_test_email(email):
		print('Sending test email to: {}'.format(email))


	def __repr__(self):
		return self.campaign

	def __getattr__(self, attr):
		if attr == 'users': # For users we are returning the `recipients.users` list
			return self.recipients.users
		else: 
			raise AttributeError