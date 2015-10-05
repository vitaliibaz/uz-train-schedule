import unittest

from src.train_route import TrainRoute
from src.station import Station


class TestTrainRoute(unittest.TestCase):
	def test_constructor(self):
		departure_station = Station("VIL'NO", '')
		arrival_station = Station('Copenhagen', '')
		train_route = TrainRoute(departure_station, '23:19', arrival_station, '09:29', '49', "VIL'NO PARMA", '5/09-3/10/2015 DAILY (EXCEPT 6,7,8,9,10,11/09/2015)')

		self.assertEqual(departure_station, train_route.departure_station)
		self.assertEqual('23:19', train_route.departure_time)
		self.assertEqual('09:29', train_route.arrival_time)
		self.assertEqual(arrival_station, train_route.arrival_station)
		self.assertEqual('49', train_route.number_train)
		self.assertEqual("Vil'No Parma", train_route.route)
		self.assertEqual('5/09-3/10/2015 daily (except 6,7,8,9,10,11/09/2015)', train_route.periodicity)

	def test_replace_multiple_spaces_route(self):
		train_route = TrainRoute('', '', '', '', '', '  Київ         Ужгород  ', '')

		self.assertEqual('Київ Ужгород', train_route.route)


if __name__ == '__main__':
	unittest.main()
