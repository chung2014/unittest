import roman1
import unittest

class KnowValues(unittest.TestCase):
	know_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V') )

	def test_to_roman_known_value(self):
		'''to_roman should give known result with known input'''
		for integer, numeral in self.know_values:
			result = roman1.to_roman(integer)
			self.assertEqual(numeral, result)

if __name__ == '__main__':
	unittest.main()