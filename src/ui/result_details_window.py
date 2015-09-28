from kivy.uix.screenmanager import Screen


class ResultDetailsWindow(Screen):
	def __init__(self, **kwargs):
		super(ResultDetailsWindow, self).__init__(**kwargs)

		self.bind(on_pre_enter=self.prepare_details_window)

	def prepare_details_window(self, args):
		print('Hello, it is final window')
		# self.clear_widgets()
		details_route = self.manager.get_screen('list_all_results_window').selected_route
		print(details_route.total_time)

