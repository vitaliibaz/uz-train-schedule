from kivy.uix.screenmanager import Screen
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

from ..data_provider import load_routes
from ..route import Route


class ListAllResultsWindow(Screen):
	def __init__(self, **kwargs):
		super(ListAllResultsWindow, self).__init__(**kwargs)

		self.selected_route = None
		self.routes = None

		self.bind(on_pre_enter=self.prepare_window_all_results)

	def prepare_window_all_results(self, args):
		self.clear_widgets()
		departure_station = self.manager.get_screen('select_departure_station_window').selected_station
		arrival_station = self.manager.get_screen('select_arrival_station_window').selected_station

		self.routes = load_routes(departure_station, arrival_station)
		routes = Route.group_routes(self.routes)

		data = {}
		for i in range(len(routes)):
			route = routes[i]
			ftdt = route.first_train.departure_time
			stat = route.second_train.arrival_time
			tt = route.total_time
			if route.first_train.number_train != route.second_train.number_train:
				data[i] = {'text': '{0} - {1} ({2}h)\nз пересадкою'.format(ftdt, stat, tt), 'route': route}
			else:
				data[i] = {'text': '{0} - {1} ({2}h)\nбез пересадки'.format(ftdt, stat, tt), 'route': route}

		dict_adapter = DictAdapter(data=data,
								   args_converter=self.result_converter,
								   template='CustomListItem')

		button_back = Button(pos_hint={"right":1, "top":1}, text="Back", multiline=False, font_size=30, color = [1,1,1,1], background_color=[1,0,0,1], on_release=self.back_menu)
		message_about_list_result = Label(pos_hint={"top":1}, text="It's the search along your route.\nFind below the route that suits you.\nClick on it to display additional features", multiline=True, size_hint_y=0.25, font_size=40)
		list_view = ListView(pos_hint={"top":0.75}, adapter=dict_adapter)

		self.add_widget(button_back)
		self.add_widget(message_about_list_result)
		self.add_widget(list_view)

	def back_menu(self, args):
		self.manager.current = 'main_window'

	def result_converter(self, row_index, result):
		converted = {'text': result['text'],
					 'size_hint_y': None,
					 'window': self,
					 'route': result['route'],
					 'height': 120,
					 'manager': self.manager}
		return converted
