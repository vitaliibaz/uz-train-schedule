class Travel(object):
	"""Enter the main parameters of the trip departure station and destination station"""
	def __init__(self, from_city, to_city):
		super(Travel, self).__init__()
		self.from_city = from_city
		self.to_city = to_city


r = Travel('Kyiv', 'Oslo')
assert r.from_city == 'Kyiv'
assert r.to_city == 'Oslo'

