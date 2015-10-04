import unittest

from src.route import Route
from src.train_route import TrainRoute


class TestRoute(unittest.TestCase):
	def test_constructor(self):
		first_train = TrainRoute('КРАКІВ (ПОЛЬЩА)', '20:52', 'Мушкетове','07:15', '3310', 'ВРОЦЛАВ ЛЬВІВ', '14/09-16/10/2015 ЩОДЕННО')
		second_train = TrainRoute('ЛЬВІВ', '09:40', 'Hillerod','16:02', '74', 'ЛЬВІВ МОСКВА', 'З 29/03/2015 ЩОДЕННО (КРІМ 2/09/2015)')
		total_time_route = '19'

		route = Route(first_train, second_train, total_time_route)

		self.assertEqual(first_train, route.first_train)
		self.assertEqual(second_train, route.second_train)
		self.assertEqual(total_time_route, route.total_time)

	def test_group_all_routes_same(self):
		first_train = TrainRoute('', '', '', '', '3310', '', '')
		second_train = TrainRoute('', '', '', '', '3310', '', '')
		route_1 = Route(first_train, second_train, '12')
		route_2 = Route(first_train, second_train, '12')
		route_3 = Route(first_train, second_train, '12')
		routes = [route_1, route_2, route_3]

		grouped = Route.group_routes(routes)

		self.assertEqual(1, len(grouped))
		self.assertEqual(['3310', '3310', '12'], [grouped[0].first_train.number_train, grouped[0].second_train.number_train, grouped[0].total_time])

	def test_group_some_routes_same(self):
		# Given
		first_train_1 = TrainRoute('', '', '', '', '0', '', '')
		first_train_2 = TrainRoute('', '', '', '', '1', '', '')
		first_train_3 = TrainRoute('', '', '', '', '2', '', '')
		first_train_4 = TrainRoute('', '', '', '', '1', '', '')
		first_train_5 = TrainRoute('', '', '', '', '0', '', '')

		second_train_1 = TrainRoute('', '', '', '', '0', '', '')
		second_train_2 = TrainRoute('', '', '', '', '1', '', '')
		second_train_3 = TrainRoute('', '', '', '', '2', '', '')
		second_train_4 = TrainRoute('', '', '', '', '1', '', '')
		second_train_5 = TrainRoute('', '', '', '', '0', '', '')

		route_1 = Route(first_train_1, second_train_1, '1')
		route_2 = Route(first_train_2, second_train_2, '2')
		route_3 = Route(first_train_3, second_train_3, '3')
		route_4 = Route(first_train_4, second_train_4, '2')
		route_5 = Route(first_train_5, second_train_5, '1')
		routes = [route_1, route_2, route_3, route_4, route_5]

		# When
		grouped = Route.group_routes(routes)

		# Then
		self.assertEqual(3, len(grouped))
		self.assertEqual(['0', '0', '1'], [grouped[0].first_train.number_train, grouped[0].second_train.number_train, grouped[0].total_time])
		self.assertEqual(['1', '1', '2'], [grouped[1].first_train.number_train, grouped[1].second_train.number_train, grouped[1].total_time])
		self.assertEqual(['2', '2', '3'], [grouped[2].first_train.number_train, grouped[2].second_train.number_train, grouped[2].total_time])

	def test_group_only_if_all_parameters_match(self):
		# Given
		first_train_1 = TrainRoute('', '', '', '', '0', '', '')
		first_train_2 = TrainRoute('', '', '', '', '0', '', '')
		first_train_3 = TrainRoute('', '', '', '', '0', '', '')
		second_train_1 = TrainRoute('', '', '', '', '1', '', '')
		second_train_2 = TrainRoute('', '', '', '', '1', '', '')
		second_train_3 = TrainRoute('', '', '', '', '1', '', '')
		route_1 = Route(first_train_1, second_train_1, '4')
		route_2 = Route(first_train_2, second_train_2, '5')
		route_3 = Route(first_train_3, second_train_3, '6')
		routes = [route_1, route_2, route_3]
		# When
		grouped = Route.group_routes(routes)
		# Then
		self.assertEqual(3, len(grouped))
		self.assertEqual(['0', '1', '4'], [grouped[0].first_train.number_train, grouped[0].second_train.number_train, grouped[0].total_time])
		self.assertEqual(['0', '1', '5'], [grouped[1].first_train.number_train, grouped[1].second_train.number_train, grouped[1].total_time])
		self.assertEqual(['0', '1', '6'], [grouped[2].first_train.number_train, grouped[2].second_train.number_train, grouped[2].total_time])

	def test_expand_routes_only_if_all_parameters_match(self):
		# Given
		first_train_selected = TrainRoute('', '', '', '', '11', '', '')
		second_train_selected = TrainRoute('', '', '', '', '12', '', '')
		selected_route = Route(first_train_selected, second_train_selected, '1')
		first_train_2 = TrainRoute('', '', '', '', '11', '', '')
		first_train_3 = TrainRoute('', '', '', '', '11', '', '')
		first_train_4 = TrainRoute('', '', '', '', '11', '', '')
		first_train_5 = TrainRoute('', '', '', '', '14', '', '')
		second_train_2 = TrainRoute('', '', '', '', '12', '', '')
		second_train_3 = TrainRoute('', '', '', '', '12', '', '')
		second_train_4 = TrainRoute('', '', '', '', '13', '', '')
		second_train_5 = TrainRoute('', '', '', '', '12', '', '')
		route_2 = Route(first_train_2, second_train_2, '1')
		route_3 = Route(first_train_3, second_train_3, '2')
		route_4 = Route(first_train_4, second_train_4, '1')
		route_5 = Route(first_train_4, second_train_4, '1')
		routes =  [selected_route, route_2, route_3, route_4, route_5]

		# When
		unfolded = Route.unfold_routes(selected_route, routes)

		# Then
		self.assertEqual(2, len(unfolded))
		self.assertEqual(['11', '12', '1'], [unfolded[0].first_train.number_train, unfolded[0].second_train.number_train, unfolded[0].total_time])
		self.assertEqual(['11', '12', '1'], [unfolded[1].first_train.number_train, unfolded[1].second_train.number_train, unfolded[1].total_time])

	def test_expand_returns_only_selected_when_no_other_matches(self):
		# Given
		first_train_selected = TrainRoute('', '', '', '', '11', '', '')
		second_train_selected = TrainRoute('', '', '', '', '15', '', '')
		selected_route = Route(first_train_selected, second_train_selected, '1')
		first_train_2 = TrainRoute('', '', '', '', '12', '', '')
		second_train_2 = TrainRoute('', '', '', '', '16', '', '')
		route_2 = Route(first_train_2, second_train_2, '1')
		routes = [selected_route, route_2]

		# When
		unfolded = Route.unfold_routes(selected_route, routes)

		# Then
		self.assertEqual(1, len(unfolded))
		self.assertEqual(['11', '15', '1'], [unfolded[0].first_train.number_train, unfolded[0].second_train.number_train, unfolded[0].total_time])

	def test_expand_returns_empty_list_when_routes_has_no_matches(self):
		# Given
		first_train_selected = TrainRoute('', '', '', '', '14', '', '')
		second_train_selected = TrainRoute('', '', '', '', '18', '', '')
		selected_route = Route(first_train_selected, second_train_selected, '1')
		first_train_2 = TrainRoute('', '', '', '', '13', '', '')
		second_train_2 = TrainRoute('', '', '', '', '17', '', '')
		route_2 = Route(first_train_2, second_train_2, '1')
		routes = [route_2]

		# When
		unfolded = Route.unfold_routes(selected_route, routes)

		# Then
		self.assertEqual(0, len(unfolded))


if __name__ == '__main__':
	unittest.main()
