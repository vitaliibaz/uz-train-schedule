import unittest

from src.train_route import TrainRoute


class TestTrainRoute(unittest.TestCase):
	def test_constructor(self):
		train_route = TrainRoute("Vil'no", '23:19', '09:29', '49', "VIL'NO PARMA", '5/09-3/10/2015 DAILY (EXCEPT 6,7,8,9,10,11/09/2015)')

		self.assertEqual("Vil'no", train_route.departure_station)
		self.assertEqual('23:19', train_route.departure_time)
		self.assertEqual('09:29', train_route.arrival_time)
		self.assertEqual('49', train_route.number_train)
		self.assertEqual("Vil'no Parma", train_route.route)
		self.assertEqual('5/09-3/10/2015 daily (except 6,7,8,9,10,11/09/2015)', train_route.periodicity)

if __name__ == '__main__':
	unittest.main()
