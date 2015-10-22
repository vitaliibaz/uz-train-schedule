import unicodedata
from kivy.uix.screenmanager import Screen


class MainWindow(Screen):
	def __init__(self, **kwargs):
		super(MainWindow, self).__init__(**kwargs)

		self.select_station_button_was_pressed = False

		self.bind(on_pre_enter=self.display_selected_stations)

	def display_selected_stations(self, args):
		self.ids.departure.text = 'Станція відправлення'
		self.ids.arrival.text = 'Станція прибуття'
		self.ids.start_search.text = 'Почати пошук'
		if self.select_station_button_was_pressed == True:
			departure_select_station_window = self.manager.get_screen('select_departure_station_window')
			arrival_select_station_window = self.manager.get_screen('select_arrival_station_window')
			if departure_select_station_window.selected_station != None:
				self.ids.departure.text = 'Від: {}'.format(departure_select_station_window.selected_station.name)
			if arrival_select_station_window.selected_station != None:
				self.ids.arrival.text = 'До: {}'.format(arrival_select_station_window.selected_station.name)
			if departure_select_station_window.selected_station != None and arrival_select_station_window.selected_station != None:
				self.ids.start_search.disabled = False

