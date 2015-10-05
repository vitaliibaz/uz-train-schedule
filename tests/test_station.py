import unittest

from src.station import Station


class TestStation(unittest.TestCase):
	def test_constructor(self):
		station = Station('Lviv', '777')

		self.assertEqual('Lviv', station.name)
		self.assertEqual('777', station.id_numbers)


	def test_matches_is_case_insensitive(self):
		station = Station('Киев', '')

		self.assertTrue(station.matches('Ки'))
		self.assertTrue(station.matches('КИ'))

	def test_matches_middle_of_name(self):
		station = Station('Кишинев', '')

		self.assertTrue(station.matches('ишинев'))

	def test_doesnt_match_other_letters(self):
		station = Station('Киев', '')

		self.assertEqual(False, station.matches('жЖ'))

	def test_matches_international_i_letters(self):
		for alpha in 'ыиі':
			station = Station('К{0}ев'.format(alpha), '')

			self.assertTrue(station.matches('ы'))
			self.assertTrue(station.matches('и'))
			self.assertTrue(station.matches('і'))

	def test_matches_international_e_letters(self):
		for alpha in 'еэє':
			station = Station('К{0}сів'.format(alpha), '')

			self.assertTrue(station.matches('е'))
			self.assertTrue(station.matches('э'))
			self.assertTrue(station.matches('є'))

	def test_matches_complex_international_letters(self):
		station = Station('КікыкиКєкекэкие', '')

		self.assertTrue(station.matches('кИкІкЫкЭкЄкЕкиї'))

	def test_shorten_russia(self):
		station = Station('Москва (Російська Федерація)', '')

		self.assertEqual('Москва (РФ)', station.name)

	def test_shorten_word_city(self):
		station = Station('Одеса Місто (Україна)', '')

		self.assertEqual('Одеса (Україна)', station.name)

	def test_station_caps(self):
		station = Station('ОДЕСА-ГОЛОВНА (УКРАЇНА)', '')

		self.assertEqual('Одеса-Головна (Україна)', station.name)

if __name__ == '__main__':
	unittest.main()
