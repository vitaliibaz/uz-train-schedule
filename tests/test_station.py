import unittest

from src.station import Station


class TestStation(unittest.TestCase):
	def test_constructor(self):
		station = Station('Lviv', '777')

		self.assertEqual('Lviv', station.name)
		self.assertEqual('777', station.id_numbers)

if __name__ == '__main__':
	unittest.main()
