import string

class Train_route(object):
	"""docstring for Train_route"""
	def __init__(self, departure_station, departure_time, arrival_time, number_train, route, periodicity):
		super(Train_route, self).__init__()
		self.departure_station = departure_station
		self.departure_time = departure_time
		self.arrival_time = arrival_time
		self.number_train = number_train
		self.route = string.capwords(route)
		self.periodicity = string.capwords(periodicity)

instance = Train_route("Vil'no", '23:19', '09:29', '49', "VIL'NO PARMA", '5/09-3/10/2015 DAILY (EXCEPT 6,7,8,9,10,11/09/2015)')
assert instance.departure_station == "Vil'no"
assert instance.departure_time == '23:19'
assert instance.arrival_time == '09:29'
assert instance.number_train == '49'
assert instance.route == "Vil'no Parma"
assert instance.periodicity == '5/09-3/10/2015 Daily (except 6,7,8,9,10,11/09/2015)'




		