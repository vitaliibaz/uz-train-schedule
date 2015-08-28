class Station(object):
	"""Enter the main parameters of the station: the name and number"""
	def __init__(self, name, id_number):
		super(Station, self).__init__()
		self.name = name
		self.id_number = id_number
