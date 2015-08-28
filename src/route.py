class Route(object):
	def __init__(self, first_train, second_train, total_time):
		super(Route, self).__init__()
		self.first_train = first_train
		self.second_train = second_train
		self.total_time = total_time
