from kivy.uix.screenmanager import Screen
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button




class ListAllResultsWindow(Screen):
	def __init__(self, **kwargs):
		kwargs['cols'] = 1
		super(ListAllResultsWindow, self).__init__(**kwargs)

		data = {}
		for i in range(100):
			data[str(i)] = {'text': '11:19 - 09:13 (16h)\nvia: Vinnitsya', 'is_selected': False}


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
					 'is_selected': result['is_selected'],
					 'size_hint_y': None,
					 'height': 120,
					 'manager': self.manager}
		return converted
