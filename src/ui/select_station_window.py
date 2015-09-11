from kivy.uix.screenmanager import Screen
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput

from ..data_provider import load_stations


class SelectStationWindow(Screen):
	def __init__(self, **kwargs):
		super(SelectStationWindow, self).__init__(**kwargs)

		self.stations = load_stations()

		filter_station = TextInput(pos_hint={"top":1}, hint_text='Start typing station name', multiline=False, size_hint_y=None, font_size=50)
		filter_station.bind(text=self.on_filter_changed)

		dict_adapter = self.prepare_stations_dict_adapter(self.stations, '')
		self.list_view = ListView(pos_hint={"top":0.85}, adapter=dict_adapter)

		self.add_widget(filter_station)
		self.add_widget(self.list_view)

	def station_converter(self, row_index, station):
		converted = {'text': station.name,
					 'size_hint_y': None,
					 'height': 120,
					 'manager': self.manager}
		return converted

	def on_filter_changed(self, filter_station, filter_text):
		dict_adapter = self.prepare_stations_dict_adapter(self.stations, filter_text)
		self.remove_widget(self.list_view)
		self.list_view = ListView(pos_hint={"top":0.85}, adapter=dict_adapter)
		self.add_widget(self.list_view)

	def prepare_stations_dict_adapter(self, stations, filter_text):
		data = {}
		for number in range(len(stations)):
			station = stations[number]
			if filter_text in station.name:
				data[str(number)] = station


		dict_adapter = DictAdapter(data=data,
								   args_converter=self.station_converter,
								   template='StationTemplate')
		return dict_adapter
