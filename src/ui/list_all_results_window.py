from kivy.uix.gridlayout import GridLayout
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class ListAllResultsWindow(GridLayout):
	def __init__(self, **kwargs):
		kwargs['cols'] = 1
		super(ListAllResultsWindow, self).__init__(**kwargs)

		data = {}
		for i in range(100):
			data[str(i)] = {'text': '11:19 — 09:13 (16h)\nvia: Vinnitsya', 'is_selected': False}


		dict_adapter = DictAdapter(data=data,
								   args_converter=self.result_converter,
								   template='CustomListItem')

		message_about_list_result = Label(text="It's the search along your route.\nFind below the route that suits you.\nClick on it to display additional features", multiline=True, size_hint_y=0.5, font_size=40)
		list_view = ListView(adapter=dict_adapter)

		self.add_widget(message_about_list_result)
		self.add_widget(list_view)



	def result_converter(self, row_index, result):
		converted = {'text': result['text'],
					 'is_selected': result['is_selected'],
					 'size_hint_y': None,
					 'height': 120}
		return converted
