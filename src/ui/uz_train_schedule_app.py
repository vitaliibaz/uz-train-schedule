import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from .main_window import MainWindow
from .select_station_window import SelectStationWindow
from .list_all_results_window import ListAllResultsWindow
from .result_details_window import ResultDetailsWindow


class UZTrainScheduleApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MainWindow(name='main_window'))
		sm.add_widget(SelectStationWindow(name='select_departure_station_window'))
		sm.add_widget(SelectStationWindow(name='select_arrival_station_window'))
		sm.add_widget(ListAllResultsWindow(name='list_all_results_window'))
		sm.add_widget(ResultDetailsWindow(name='result_details_window'))
		return sm


def run():
	Builder.load_file("src/ui/main_window.kv")
	Builder.load_file("src/ui/select_station_window.kv")
	Builder.load_file("src/ui/list_all_results_window.kv")
	Builder.load_file("src/ui/result_details_window.kv")

	UZTrainScheduleApp().run()


if __name__ == "__main__":
	run()
