from __future__ import unicode_literals


class Station(object):
	"""Enter the main parameters of the station: the name and number"""
	def __init__(self, name, id_numbers):
		super(Station, self).__init__()
		self.name = name.title().replace('Російська Федерація', 'РФ').replace(' Місто ', ' ').strip()
		self.id_numbers = id_numbers.strip()

	def matches(self, filter_text):
		filter_text = filter_text                                 \
			.lower()                                              \
			.replace('ы', 'и')    \
			.replace('і', 'и')    \
			.replace('э', 'е')    \
			.replace('є', 'е')    \
			.replace('ие', 'иї')  \

		name = self.name                                          \
			.lower()                                              \
			.replace('ы', 'и')    \
			.replace('і', 'и')    \
			.replace('э', 'е')    \
			.replace('є', 'е')    \
			.replace('ие', 'иї')  \

		if filter_text in name:
			return True
		else:
			return False
