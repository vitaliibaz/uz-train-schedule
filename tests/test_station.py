from sys import path
path.append('../src')

from station import Station

station_name = Station('Lviv', 777)
assert station_name.name == 'Lviv'
assert station_name.id_number == 777
