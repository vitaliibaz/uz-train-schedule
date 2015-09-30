from kivy.uix.screenmanager import Screen


class ResultDetailsWindow(Screen):
	def __init__(self, **kwargs):
		super(ResultDetailsWindow, self).__init__(**kwargs)

		self.bind(on_pre_enter=self.prepare_details_window)

	def prepare_details_window(self, args):
		details_route = self.manager.get_screen('list_all_results_window').selected_route

		self.ids.departure.text = details_route.first_train.departure_station.name
		self.ids.arrival.text = details_route.second_train.arrival_station.name
		if details_route.first_train.number_train != details_route.second_train.number_train:
			self.ids.via.text = '{0} - {1} {2}'.format(details_route.first_train.arrival_time, details_route.second_train.departure_time, details_route.second_train.departure_station.name)
		else:
			self.ids.via.text = 'без пересадки'
		self.ids.departure_time.text = details_route.first_train.departure_time
		self.ids.arrival_time.text = details_route.second_train.arrival_time
		self.ids.total_time.text = details_route.total_time
		self.ids.periodicity.text = details_route.first_train.periodicity
		self.ids.number_train_and_route.text = '{0} {1}'.format(details_route.first_train.number_train, details_route.first_train.route)

