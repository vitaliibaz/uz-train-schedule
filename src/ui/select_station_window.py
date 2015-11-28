# coding=utf-8
from __future__ import unicode_literals
from kivy.uix.screenmanager import Screen
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput
import requests

from ..data_provider import load_stations


class SelectStationWindow(Screen):
    try:
        stations = load_stations()
    except requests.exceptions.RequestException as err:
        stations = None

    def __init__(self, **kwargs):
        super(SelectStationWindow, self).__init__(**kwargs)

        self.selected_station = None

        self.bind(on_pre_enter=self.prepare)

    def prepare(self, args):

        self.clear_widgets()
        filter_station = TextInput(pos_hint={"top":1}, hint_text='Почніть вводити назву станції', size_hint_y=0.07, font_size='20sp')
        filter_station.bind(text=self.on_filter_changed)

        dict_adapter = self.prepare_stations_dict_adapter(self.stations, '')
        self.list_view = ListView(pos_hint={"top":0.93}, adapter=dict_adapter)

        self.add_widget(filter_station)
        self.add_widget(self.list_view)

    def station_converter(self, row_index, station):
        converted = {'text': station.name,
                     'size_hint_y': None,
                     'height': '60sp',
                     'station': station,
                     'window': self,
                     'manager': self.manager}
        return converted

    def on_filter_changed(self, filter_station, filter_text):
        dict_adapter = self.prepare_stations_dict_adapter(self.stations, filter_text.decode('utf-8'))
        self.remove_widget(self.list_view)
        self.list_view = ListView(pos_hint={"top":0.93}, adapter=dict_adapter)
        self.add_widget(self.list_view)

    def prepare_stations_dict_adapter(self, stations, filter_text):
        data = {}
        for number in range(len(stations)):
            station = stations[number]
            if station.matches(filter_text) is True:
                data[number] = station


        dict_adapter = DictAdapter(data=data,
                                   args_converter=self.station_converter,
                                   template=b'StationTemplate')
        return dict_adapter
