import requests
from station import Station

def load_stations():
	address = 'http://www.uz.gov.ua/passengers/timetables/suggest-station/'
	station_strings = requests.get(address, headers={"User-Agent": "Mozilla"}).json()
	stations = []

	for station_string in station_strings:
		parts = station_string.split('~')
		station = Station(parts[0], parts[1])
		stations.append(station)

	return stations
