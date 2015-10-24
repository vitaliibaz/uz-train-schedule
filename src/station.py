# coding=utf-8


class Station(object):
	"""Enter the main parameters of the station: the name and number"""
	def __init__(self, name, id_numbers):
		super(Station, self).__init__()
		self.name = name.title().replace('Російська Федерація'.decode('utf-8'), 'РФ'.decode('utf-8')).replace(' Місто '.decode('utf-8'), ' '.decode('utf-8')).strip()
		self.id_numbers = id_numbers.strip()

	def matches(self, filter_text):
		filter_text = filter_text                                 \
			.lower()                                              \
			.replace(u'ы', u'и')    \
			.replace(u'і', u'и')    \
			.replace(u'э', u'е')    \
			.replace(u'є', u'е')    \
			.replace(u'ие', u'иї')  \

		name = self.name                                          \
			.lower()                                              \
			.replace(u'ы', u'и')    \
			.replace(u'і', u'и')    \
			.replace(u'э', u'е')    \
			.replace(u'є', u'е')    \
			.replace(u'ие', u'иї')  \

		if filter_text in name:
			return True
		else:
			return False
