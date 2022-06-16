import unittest
from testing import keliamieji


class TestKeliamieji3(unittest.TestCase):
    def setUp(self):
        self.objektas = keliamieji()

    def test_tikrinti(self):
        self.assertTrue(self.objektas.tikrinti(2000))
        self.assertTrue(self.objektas.tikrinti(2020))
        self.assertFalse(self.objektas.tikrinti(2100))

    def test_diapazonas(self):
        rezultatas = self.objektas.diapazonas(1980, 2000)
        lukestis = [1980, 1984, 1988, 1992, 1996]
        self.assertEqual(lukestis, rezultatas)