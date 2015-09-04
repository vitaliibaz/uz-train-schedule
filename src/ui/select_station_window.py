from kivy.uix.screenmanager import Screen
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput


class SelectStationWindow(Screen):
	def __init__(self, **kwargs):
		super(SelectStationWindow, self).__init__(**kwargs)

		data = {}
		for i in range(100):
			data[str(i)] = {'text': 'Station ' + str(i), 'is_selected': False}


		dict_adapter = DictAdapter(data=data,
								   args_converter=self.station_converter,
								   template='StationTemplate')

		filter_station = TextInput(pos_hint={"top":1}, hint_text='Start typing station name', multiline=False, size_hint_y=None, font_size=50)
		list_view = ListView(pos_hint={"top":0.85}, adapter=dict_adapter)

		self.add_widget(filter_station)
		self.add_widget(list_view)



	def station_converter(self, row_index, station):
		converted = {'text': station['text'],
					 'is_selected': station['is_selected'],
					 'size_hint_y': None,
					 'height': 120,
					 'manager': self.manager}
		return converted
