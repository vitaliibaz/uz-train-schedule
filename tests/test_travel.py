from sys import path
path.append('..')

import unittest
from src.travel import Travel

class TestTravel(unittest.TestCase):
	def test_constructor(self):
		travel = Travel('Kyiv', 'Oslo')

		self.assertEqual('Kyiv', travel.from_city)
		self.assertEqual('Oslo', travel.to_city)

if __name__ == '__main__':
	unittest.main()
