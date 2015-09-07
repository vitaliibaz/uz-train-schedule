from sys import path
path.append('..')

from kivy.uix.screenmanager import Screen
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput

from data_provider import load_stations


class SelectStationWindow(Screen):
	def __init__(self, **kwargs):
		super(SelectStationWindow, self).__init__(**kwargs)

		stations = load_stations()
		data = {}
		for number in range(len(stations)):
			data[str(number)] = stations[number]


		dict_adapter = DictAdapter(data=data,
								   args_converter=self.station_converter,
								   template='StationTemplate')

		filter_station = TextInput(pos_hint={"top":1}, hint_text='Start typing station name', multiline=False, size_hint_y=None, font_size=50)
		list_view = ListView(pos_hint={"top":0.85}, adapter=dict_adapter)

		self.add_widget(filter_station)
		self.add_widget(list_view)

	def station_converter(self, row_index, station):
		converted = {'text': station.name,
					 'size_hint_y': None,
					 'height': 120,
					 'manager': self.manager}
		return converted
