import unittest
from city_function import city_country


class CityTestCase(unittest.TestCase):
    """test city_function.py"""

    def test_city_country(self):
        citycountry = city_country('santiago', 'chile')
        self.assertEqual(citycountry, 'Santiago, Chile')

    def test_city_country_population(self):
        citycountry = city_country('santiago', 'chile', '5000000')
        self.assertEqual(citycountry, 'Santiago, Chile - population 5000000')

unittest.main()
