# coding=utf-8
from kivy.uix.screenmanager import Screen

from ..data_provider import load_routes
from ..route import Route


class ResultDetailsWindow(Screen):
	def __init__(self, **kwargs):
		super(ResultDetailsWindow, self).__init__(**kwargs)

		self.bind(on_pre_enter=self.prepare_details_window)

	def prepare_details_window(self, args):
		details_route = self.manager.get_screen('list_all_results_window').selected_route

		departure_station = details_route.first_train.departure_station
		# TODO #60
		# arrival_station  = details_route.second_train.arrival_station
		arrival_station = self.manager.get_screen('select_arrival_station_window').selected_station

		self.ids.departure.text = 'Від: {0} - {1}'.decode('utf-8').format(details_route.first_train.departure_time, departure_station.name)
		self.ids.arrival.text = 'До:  {0} - {1}'.decode('utf-8').format(details_route.second_train.arrival_time, arrival_station.name)
		self.ids.total_time.text = 'Час в дорозі: {0} год.'.decode('utf-8').format(details_route.total_time)
		self.ids.number_train_and_route.text = 'Відправлення: поїзд {0} {1}'.decode('utf-8').format(details_route.first_train.number_train, details_route.first_train.route)

		routes = self.manager.get_screen('list_all_results_window').routes
		unfolded_routes = Route.unfold_routes(details_route, routes)

		self.ids.periodicity_first_train.text = ''
		self.ids.via.text = ''
		self.ids.periodicity_second_train.text = ''
		self.ids.transfer.text = ''

		for route in unfolded_routes:
			periodicity_1 = route.first_train.periodicity + '\n'
			if periodicity_1 not in self.ids.periodicity_first_train.text:
				self.ids.periodicity_first_train.text += periodicity_1

		if details_route.first_train.number_train == details_route.second_train.number_train:
			self.ids.via.text = 'Без пересадки'.decode('utf-8')
		else:
			self.ids.transfer.text = 'Час очікування і станція пересадки:\n'.decode('utf-8')
			self.ids.via.text = 'Пересадка: поїзд {0} {1}\n'.decode('utf-8').format(details_route.second_train.number_train, route.second_train.route)

			for route in unfolded_routes:
				arrival_transfer = route.first_train.arrival_time
				departure_transfer = route.second_train.departure_time
				station_transfer = route.second_train.departure_station.name

				transfer_info = 'з {0} до {1} - {2}\n'.decode('utf-8').format(arrival_transfer, departure_transfer, station_transfer)
				if transfer_info not in self.ids.transfer.text:
					self.ids.transfer.text += transfer_info

				periodicity_2 = route.second_train.periodicity + '\n'
				if periodicity_2 not in self.ids.periodicity_second_train.text:
					self.ids.periodicity_second_train.text += periodicity_2
