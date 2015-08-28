import string

class TrainRoute(object):
	"""Received basic parameters of the train trip: departure station, arrival station, train number, route (starting and ending station), departure and arrival time, frequency of movement"""
	def __init__(self, departure_station, departure_time, arrival_time, number_train, route, periodicity):
		super(TrainRoute, self).__init__()
		self.departure_station = departure_station
		self.departure_time = departure_time
		self.arrival_time = arrival_time
		self.number_train = number_train
		self.route = string.capwords(route)
		self.periodicity = periodicity.lower()
