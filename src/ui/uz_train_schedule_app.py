import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

from main_window import MainWindow
from select_station_window import SelectStationWindow
from list_all_results_window import ListAllResultsWindow


class UZTrainScheduleApp(App):
    def build(self):
        return ListAllResultsWindow()

if __name__ == "__main__":
	Builder.load_file("main_window.kv")
	Builder.load_file("select_station_window.kv")
	Builder.load_file("list_all_results_window.kv")

	UZTrainScheduleApp().run()
