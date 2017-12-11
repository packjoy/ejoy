# Module based imports
from packjoy.mail.mail_helpers import send_email_to

# Relative imports
from .campaigns import PriceDecrease, BackInStock, Welcome, NewArrivals
from .recipients import Recipients


class Newsletter(object):


	def __init__(self, filters=[], campaign_type=None):
		self.recipients = Recipients(filters)
		self.campaign = self.create_campaign(campaign_type)


	def send_test_email(self, email):
		print('Sending test email to: {}'.format(email))
		send_email_to(email_address=email, template=self.campaign.template)


	@staticmethod
	def create_campaign(campaign_type):
		if campaign_type == 'price_decrease':
			return PriceDecrease()
		elif campaign_type == 'back_in_stock':
			return BackInStock()
		elif campaign_type == 'welcome':
			return Welcome()
		elif campaign_type == 'new_arrivals':
			return NewArrivals()
		else:
			raise NotImplementedError('campaign_type: {} is not implemented yet'.format(campaign_type))





	def __repr__(self):
		return self.campaign


	def __getattr__(self, attr):
		if attr == 'users': # For users we are returning the `recipients.users` list
			return self.recipients.users
		else: 
			raise AttributeError