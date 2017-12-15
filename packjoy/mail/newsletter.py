# Module based imports
from packjoy.mail.mail_helpers import send_email_to
from packjoy.common.models import Token

# Relative imports
from .campaigns import PriceDecrease, BackInStock, Welcome, NewArrivals
from .recipients import Recipients


class Newsletter(object):
	'''

	This will send the emails

	# campaign_type will select the campaign
	# users a list of USERS which whom u send the email
	# filters a list of filters to choose the recipient

	There are 2 way you can select recipients:
		- giving a list of USER objects
		- giving a list of filters which we'll use to
		query the users

	'''
	# KIND OF HACK!
	starter_coupon = Token.query.filter_by(token_code='PACKJOYST').first()

	def __init__(self, campaign_type=None, users=None, filters=[], template=None):
		self.recipients = Recipients(filters=filters, users=users)
		self.campaign = self.create_campaign(campaign_type, template=template)


	def send_test_email(self, email):
		print('Sending test email to: {}'.format(email))
		send_email_to(email_address=email, template=self.campaign.template)

	def send_emails(self):
		for user in self.users:
			for email in user.emails:
				send_email_to(email_address=email.email, template=self.campaign.template)

	def create_campaign(self, campaign_type, template_name):
		if campaign_type == 'price_decrease':
			return PriceDecrease(template_name=template_name)
		elif campaign_type == 'back_in_stock':
			return BackInStock(template_name=template_name)
		elif campaign_type == 'welcome':
			return Welcome(token=self.starter_coupon, template_name=template_name)
		elif campaign_type == 'new_arrivals':
			return NewArrivals(template_name=template_name)
		else:
			raise NotImplementedError('campaign_type: {} is not implemented yet'.format(campaign_type))





	def __repr__(self):
		return self.campaign


	def __getattr__(self, attr):
		if attr == 'users': # For users we are returning the `recipients.users` list
			return self.recipients.users
		else:
			raise AttributeError('ERROR')