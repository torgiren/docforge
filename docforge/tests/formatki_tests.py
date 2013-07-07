import unittest

from pyramid import testing
from functions import DummyMongo

from docforge.views.formatki import FormatkiView
from docforge.errors import *

class FormatkiTests(unittest.TestCase):
    def setUp(self):
        self.db = DummyMongo()
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        self.request.db = self.db.create()

        self.dictionary = {}
        self.dictionary['nazwa_1'] = "imie"
        self.dictionary['typ_1'] = "tekst"
        self.dictionary['nazwa_2'] = "nazwisko"
        self.dictionary['typ_2'] = "liczba"
        self.dictionary['nazwa'] = "formularz"
        self.dictionary['nazwa_10'] = "wiek"
        self.dictionary['typ_10'] = 'liczba'
        self.formatka = FormatkiView(self.request)

    def tearDown(self):
        self.db.delete()
        testing.tearDown()

    def test_merge_fields_merge(self):
        self.assertEqual(self.formatka._merge_field(self.dictionary), [('nazwa_1', 'typ_1'), ('nazwa_10', 'typ_10'), ('nazwa_2', 'typ_2')])

    def test_merge_fields_length_mismach(self):
        self.dictionary['nazwa_11'] = 'kubatura'
        self.assertRaises(LengthMismachException, self.formatka._merge_field, self.dictionary)
