# coding=utf-8
from __future__ import unicode_literals
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

        self.departure_station = None
        self.arrival_station = None

        self.bind(on_pre_enter=self.prepare_window_all_results)

    def prepare_window_all_results(self, args):
        new_departure_station = self.manager.get_screen('select_departure_station_window').selected_station
        new_arrival_station = self.manager.get_screen('select_arrival_station_window').selected_station

        if self.departure_station != new_departure_station or self.arrival_station != new_arrival_station:
            self.routes = load_routes(new_departure_station, new_arrival_station)
            routes = Route.group_routes(self.routes)

            data = {}
            for i in range(len(routes)):
                route = routes[i]
                ftdt = route.first_train.departure_time
                stat = route.second_train.arrival_time
                tt = route.total_time
                if route.first_train.number_train != route.second_train.number_train:
                    data[i] = {'text': '{0} - {1} ({2} год.)\nз пересадкою'.format(ftdt, stat, tt), 'route': route}
                else:
                    data[i] = {'text': '{0} - {1} ({2} год.)\nбез пересадки'.format(ftdt, stat, tt), 'route': route}

            dict_adapter = DictAdapter(data=data,
                                       args_converter=self.result_converter,
                                       template=b'CustomListItem')

            message_about_list_result = Label(pos_hint={"top":1}, text='Від: {0}\nДо:  {1}'.format(new_departure_station.name, new_arrival_station.name), multiline=True, size_hint_y=0.25, font_size=40)
            list_view = ListView(pos_hint={"top":0.75}, adapter=dict_adapter)

            self.clear_widgets()

            self.add_widget(message_about_list_result)
            self.add_widget(list_view)

            self.departure_station = new_departure_station
            self.arrival_station = new_arrival_station

    def result_converter(self, row_index, result):
        converted = {'text': result['text'],
                     'size_hint_y': None,
                     'window': self,
                     'route': result['route'],
                     'height': 120,
                     'manager': self.manager}
        return converted
