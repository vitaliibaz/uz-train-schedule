from sys import path
path.append('../src')

import unittest
from route import Route

class TestRoute(unittest.TestCase):
	def test_constructor(self):
		route = Route(14121, 777, 14)

		self.assertEqual(14121, route.first_train)
		self.assertEqual(777, route.second_train)
		self.assertEqual(14, route.total_time)

if __name__ == '__main__':
	unittest.main()
