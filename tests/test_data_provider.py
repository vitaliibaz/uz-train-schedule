from sys import path
path.append('../src')

import unittest

from data_provider import load_routes
from station import Station
from route import Route


class TestDataProvider(unittest.TestCase):
	def test_load_routes(self):
		first_station = Station('Краків (Польща)', '2157,2305')
		second_station = Station('Вінниця (Україна)', '22200')

		routes = load_routes(first_station, second_station)

		self.assertEqual(56, len(routes))
		for route in routes:
			self.assertEqual(Route, type(route))


if __name__ == '__main__':
	unittest.main()