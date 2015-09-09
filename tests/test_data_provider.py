import unittest

from src.data_provider import load_routes, load_stations
from src.station import Station
from src.route import Route


class TestDataProvider(unittest.TestCase):
	def test_load_stations(self):
		stations = load_stations()

		for station in stations:
			self.assertEqual(Station, type(station))

	def test_load_routes(self):
		first_station = Station('Краків (Польща)', '2157,2305')
		second_station = Station('Вінниця (Україна)', '22200')

		routes = load_routes(first_station, second_station)

		for route in routes:
			self.assertEqual(Route, type(route))


if __name__ == '__main__':
	unittest.main()
