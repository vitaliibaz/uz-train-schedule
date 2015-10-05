class TrainRoute(object):
	"""Received basic parameters of the train trip: departure station, arrival station, train number, route (starting and ending station), departure and arrival time, frequency of movement"""
	def __init__(self, departure_station, departure_time, arrival_station, arrival_time, number_train, route, periodicity):
		super(TrainRoute, self).__init__()
		self.departure_station = departure_station
		self.departure_time = departure_time.strip()
		self.arrival_station = arrival_station
		self.arrival_time = arrival_time.strip()
		self.number_train = number_train.strip()
		self.route = ' '.join(route.split()).title()
		self.periodicity = periodicity.lower().strip()
