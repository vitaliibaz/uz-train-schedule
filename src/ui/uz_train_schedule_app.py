# coding=utf-8
from __future__ import unicode_literals
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.base import EventLoop

from .main_window import MainWindow
from .select_station_window import SelectStationWindow
from .list_all_results_window import ListAllResultsWindow
from .result_details_window import ResultDetailsWindow


class UZTrainScheduleApp(App):

    def build(self):
        self.bind(on_start=self.post_build_init)

        self.manager = ScreenManager()
        self.manager.add_widget(MainWindow(name='main_window'))
        self.manager.add_widget(SelectStationWindow(name='select_departure_station_window'))
        self.manager.add_widget(SelectStationWindow(name='select_arrival_station_window'))
        self.manager.add_widget(ListAllResultsWindow(name='list_all_results_window'))
        self.manager.add_widget(ResultDetailsWindow(name='result_details_window'))
        return self.manager

    def post_build_init(self, *args):
        if platform() == 'android':
            import android
            android.map_key(android.KEYCODE_BACK, 1001)

        window = EventLoop.window
        window.bind(on_keyboard=self.on_keyboard)

    def on_keyboard(self, window, keycode, keycode2, text, modifiers):
        if keycode in [27, 1001]:
            if self.manager.current in ['select_departure_station_window', 'select_arrival_station_window', 'list_all_results_window']:
                self.manager.current = 'main_window'
                return True
            elif self.manager.current == 'result_details_window':
                self.manager.current = 'list_all_results_window'
                return True
            else:
                self.stop()
        return False

    def on_pause(self):
        return True

def run():
    Builder.load_file("src/ui/main_window.kv")
    Builder.load_file("src/ui/select_station_window.kv")
    Builder.load_file("src/ui/list_all_results_window.kv")
    Builder.load_file("src/ui/result_details_window.kv")

    UZTrainScheduleApp().run()


if __name__ == "__main__":
    run()
