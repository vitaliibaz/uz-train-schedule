class Station(object):
	"""Enter the main parameters of the station: the name and number"""
	def __init__(self, name, id_numbers):
		super(Station, self).__init__()
		self.name = name.title().replace(u'Російська Федерація', u'РФ').replace(u' Місто ', u' ').strip()
		self.id_numbers = id_numbers.strip()

	def matches(self, filter_text):
		filter_text = filter_text \
			.lower()              \
			.replace(u'ы', u'и')    \
			.replace(u'і', u'и')    \
			.replace(u'э', u'е')    \
			.replace(u'є', u'е')    \
			.replace(u'ие', u'иї')  \

		name = self.name          \
			.lower()              \
			.replace(u'ы', u'и')    \
			.replace(u'і', u'и')    \
			.replace(u'э', u'е')    \
			.replace(u'є', u'е')    \
			.replace(u'ие', u'иї')  \

		if filter_text in name:
			return True
		else:
			return False
