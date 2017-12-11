class Base:
	campaign_type = None
	template = '<h1>Default Campaign</h1>'

	def __repr__(self):
		return self.campaign_type


class PriceDecrease(Base):
	campaign_type = 'Price Decrease'
	pass


class BackInStock(Base):
	campaign_type = 'Back In Stock'
	pass


class Welcome(Base):
	campaign_type = 'Welcome'
	pass


class NewArrivals(Base):
	campaign_type = 'New Arrivals'
	pass