class Route(object):
	def __init__(self, first_train, second_train, total_time):
		super(Route, self).__init__()
		self.first_train = first_train
		self.second_train = second_train
		self.total_time = total_time


def filter_routes_without_transfer(routes):
	filter_routes = []
	for route in routes:
		if route.first_train.number_train != route.second_train.number_train:
			filter_routes.append(route)
		else:
			find_route = False
			for f_route in filter_routes:
				if route.first_train.number_train == f_route.first_train.number_train:
					find_route = True
					break
			if find_route == False:
				filter_routes.append(route)

	return filter_routes
