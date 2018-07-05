from city_functions import name
import unittest
class TestCase(unittest.TestCase):
    def test_city_country(self):
        Te = name("baz","sich")
        self.assertEqual(Te,"Baz, Sich - ")
unittest.main()
