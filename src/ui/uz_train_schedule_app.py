import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from main_window import MainWindow
from select_station_window import SelectStationWindow
from list_all_results_window import ListAllResultsWindow


class UZTrainScheduleApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MainWindow(name='main_window'))
		sm.add_widget(SelectStationWindow(name='select_station_window'))
		sm.add_widget(ListAllResultsWindow(name='list_all_results_window'))
		return sm


if __name__ == "__main__":
	Builder.load_file("main_window.kv")
	Builder.load_file("select_station_window.kv")
	Builder.load_file("list_all_results_window.kv")

	UZTrainScheduleApp().run()
