class Route(object):
	def __init__(self, first_train, second_train, total_time):
		super(Route, self).__init__()
		self.first_train = first_train
		self.second_train = second_train
		self.total_time = total_time

	def group_routes(routes):
		grouped = []
		for route in routes:
			find_route = False
			for f_route in grouped:
				first_trains_same = route.first_train.number_train == f_route.first_train.number_train
				second_trains_same = route.second_train.number_train == f_route.second_train.number_train
				total_time_same = route.total_time == f_route.total_time
				if first_trains_same and second_trains_same and total_time_same:
					find_route = True
					break
			if find_route == False:
				grouped.append(route)

		return grouped
