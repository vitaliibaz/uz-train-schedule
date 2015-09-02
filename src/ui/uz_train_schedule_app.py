import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

from main_window import MainWindow


class UZTrainScheduleApp(App):
    def build(self):
        return MainWindow()

if __name__ == "__main__":
	Builder.load_file("main_window.kv")

	UZTrainScheduleApp().run()
