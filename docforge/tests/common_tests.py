import unittest

from pyramid import testing
from docforge.views.common import startwith


class CommonTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

        self.x = {}
        self.x['nazwa_1'] = "imie"
        self.x['typ_1'] = "tekst"
        self.x['nazwa_2'] = "nazwisko"
        self.x['typ_2'] = "liczba"
        self.x['nazwa'] = "formularz"

    def tearDown(self):
        testing.tearDown()

    def test_startswith_nazwa(self):
        self.assertEqual(set(startwith(self.x, "nazwa_")), set(["nazwa_1", "nazwa_2"]))
