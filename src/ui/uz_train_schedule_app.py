import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout


class UZTrainScheduleApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
	Builder.load_file("uz_train_schedule.kv")
	UZTrainScheduleApp().run()
