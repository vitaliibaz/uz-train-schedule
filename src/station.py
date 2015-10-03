class Station(object):
	"""Enter the main parameters of the station: the name and number"""
	def __init__(self, name, id_numbers):
		super(Station, self).__init__()
		self.name = name.replace('Російська Федерація', 'РФ')
		self.id_numbers = id_numbers

	def matches(self, filter_text):
		filter_text = filter_text \
			.lower()              \
			.replace('ы', 'и')    \
			.replace('і', 'и')    \
			.replace('э', 'е')    \
			.replace('є', 'е')    \
			.replace('ие', 'иї')  \

		name = self.name          \
			.lower()              \
			.replace('ы', 'и')    \
			.replace('і', 'и')    \
			.replace('э', 'е')    \
			.replace('є', 'е')    \
			.replace('ие', 'иї')  \

		if filter_text in name:
			return True
		else:
			return False
