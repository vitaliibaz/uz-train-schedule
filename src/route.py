class Route(object):
	def __init__(self, first_train, second_train, total_time):
		super(Route, self).__init__()
		self.first_train = first_train
		self.second_train = second_train
		self.total_time = total_time


def filter_routes_without_transfer(routes):
	filter_routes = []
	for left_route in routes:
		find_route = False
		if left_route.first_train.number_train != left_route.second_train.number_train:
			filter_routes.append(left_route)
		else:
			if len(filter_routes) == 0:
				filter_routes.append(left_route)
			else:
				for right_route in filter_routes:
					if left_route.first_train.number_train != right_route.first_train.number_train:
						continue
					else:
						find_route = True
						break
				if find_route == False:
					filter_routes.append(left_route)

	return filter_routes
