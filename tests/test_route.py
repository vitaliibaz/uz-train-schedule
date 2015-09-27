import unittest

from src.route import Route, filter_routes_without_transfer
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

	def test_filter_all_routes_same(self):
		first_train = TrainRoute('', '', '', '3310', '', '')
		second_train = TrainRoute('', '', '', '3310', '', '')
		route_1 = Route(first_train, second_train, '')
		route_2 = Route(first_train, second_train, '')
		route_3 = Route(first_train, second_train, '')
		routes = [route_1, route_2, route_3]

		filtered = filter_routes_without_transfer(routes)

		self.assertEqual(1, len(filtered))
		self.assertEqual('3310', filtered[0].first_train.number_train)
		self.assertEqual('3310', filtered[0].second_train.number_train)

	def test_filter_some_routes_same(self):
		# Given
		first_train_1 = TrainRoute('', '', '', '0', '', '')
		first_train_2 = TrainRoute('', '', '', '1', '', '')
		first_train_3 = TrainRoute('', '', '', '2', '', '')
		first_train_4 = TrainRoute('', '', '', '1', '', '')
		first_train_5 = TrainRoute('', '', '', '0', '', '')

		second_train_1 = TrainRoute('', '', '', '0', '', '')
		second_train_2 = TrainRoute('', '', '', '1', '', '')
		second_train_3 = TrainRoute('', '', '', '2', '', '')
		second_train_4 = TrainRoute('', '', '', '1', '', '')
		second_train_5 = TrainRoute('', '', '', '0', '', '')

		route_1 = Route(first_train_1, second_train_1, '')
		route_2 = Route(first_train_2, second_train_2, '')
		route_3 = Route(first_train_3, second_train_3, '')
		route_4 = Route(first_train_4, second_train_4, '')
		route_5 = Route(first_train_5, second_train_5, '')
		routes = [route_1, route_2, route_3, route_4, route_5]

		# When
		filtered = filter_routes_without_transfer(routes)

		# Then
		self.assertEqual(3, len(filtered))
		self.assertEqual(['0', '0'], [filtered[0].first_train.number_train, filtered[0].second_train.number_train])
		self.assertEqual(['1', '1'], [filtered[1].first_train.number_train, filtered[1].second_train.number_train])
		self.assertEqual(['2', '2'], [filtered[2].first_train.number_train, filtered[2].second_train.number_train])

	def test_filter_keeps_routes_with_transfer(self):
		first_train_1 = TrainRoute('', '', '', '0', '', '')
		first_train_2 = TrainRoute('', '', '', '1', '', '')
		first_train_3 = TrainRoute('', '', '', '2', '', '')
		second_train_1 = TrainRoute('', '', '', '4', '', '')
		second_train_2 = TrainRoute('', '', '', '5', '', '')
		second_train_3 = TrainRoute('', '', '', '6', '', '')
		route_1 = Route(first_train_1, second_train_1, '')
		route_2 = Route(first_train_2, second_train_2, '')
		route_3 = Route(first_train_3, second_train_3, '')
		routes = [route_1, route_2, route_3]

		filtered = filter_routes_without_transfer(routes)

		self.assertEqual(3, len(filtered))
		self.assertEqual(['0', '4'], [filtered[0].first_train.number_train, filtered[0].second_train.number_train])
		self.assertEqual(['1', '5'], [filtered[1].first_train.number_train, filtered[1].second_train.number_train])
		self.assertEqual(['2', '6'], [filtered[2].first_train.number_train, filtered[2].second_train.number_train])


if __name__ == '__main__':
	unittest.main()
