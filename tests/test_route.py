from sys import path
path.append('..')

import unittest
from src.route import Route
from src.train_route import TrainRoute

class TestRoute(unittest.TestCase):
	def test_constructor(self):
		first_train = TrainRoute('КРАКІВ (ПОЛЬЩА)', '20:52', '07:15', '3310', 'ВРОЦЛАВ ЛЬВІВ', '14/09-16/10/2015 ЩОДЕННО')
		second_train = TrainRoute('ЛЬВІВ', '09:40', '16:02', '74', 'ЛЬВІВ МОСКВА', 'З 29/03/2015 ЩОДЕННО (КРІМ 2/09/2015)')
		total_time_route = '19'

		route = Route(first_train, second_train, total_time_route)

		self.assertEqual(first_train, route.first_train)
		self.assertEqual(second_train, route.second_train)
		self.assertEqual(total_time_route, route.total_time)

if __name__ == '__main__':
	unittest.main()
