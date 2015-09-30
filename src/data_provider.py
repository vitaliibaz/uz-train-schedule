import requests
from lxml import html

from .station import Station
from .train_route import TrainRoute
from .route import Route


def load_stations():
	address = 'http://www.uz.gov.ua/passengers/timetables/suggest-station/'
	station_strings = requests.get(address, headers={"User-Agent": "Mozilla"}).json()
	stations = []

	for station_string in station_strings:
		parts = station_string.split('~')
		station = Station(parts[0], parts[1])
		stations.append(station)

	return stations

def load_routes(first_station, second_station):
	address = 'http://www.uz.gov.ua/route_2/index.php?start_st={0}&fin_st={1}'.format(first_station.id_numbers, second_station.id_numbers)
	routes_html = requests.get(address, headers={"User-Agent": "Mozilla"}).text
	tree = html.fromstring(routes_html)
	rows = tree.xpath('//table/tr')

	routes = []
	for row in rows[4:]:
		c = row.xpath('.//td')

		transfer_station = Station(c[7].text, '')
		first_train_route = TrainRoute(first_station, c[1].text, transfer_station, c[5].text, c[2].text, c[3].text, c[4].text)
		second_train_route = TrainRoute(transfer_station, c[9].text, second_station, c[13].text, c[10].text, c[11].text, c[12].text)
		route = Route(first_train_route, second_train_route, c[15].text)
		routes.append(route)

	return routes
