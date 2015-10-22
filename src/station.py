class Station(object):
	"""Enter the main parameters of the station: the name and number"""
	def __init__(self, name, id_numbers):
		super(Station, self).__init__()
		self.name = name.title().replace('Російська Федерація'.decode('utf-8'), 'РФ'.decode('utf-8')).replace(' Місто '.decode('utf-8'), ' '.decode('utf-8')).strip()
		self.id_numbers = id_numbers.strip()

	def matches(self, filter_text):
		filter_text = filter_text                                 \
			.lower()                                              \
			.replace('ы'.decode('utf-8'), 'и'.decode('utf-8'))    \
			.replace('і'.decode('utf-8'), 'и'.decode('utf-8'))    \
			.replace('э'.decode('utf-8'), 'е'.decode('utf-8'))    \
			.replace('є'.decode('utf-8'), 'е'.decode('utf-8'))    \
			.replace('ие'.decode('utf-8'), 'иї'.decode('utf-8'))  \

		name = self.name                                          \
			.lower()                                              \
			.replace('ы'.decode('utf-8'), 'и'.decode('utf-8'))    \
			.replace('і'.decode('utf-8'), 'и'.decode('utf-8'))    \
			.replace('э'.decode('utf-8'), 'е'.decode('utf-8'))    \
			.replace('є'.decode('utf-8'), 'е'.decode('utf-8'))    \
			.replace('ие'.decode('utf-8'), 'иї'.decode('utf-8'))  \

		if filter_text in name:
			return True
		else:
			return False
