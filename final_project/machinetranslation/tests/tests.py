import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Bienvenue'), 'Welcome')
        self.assertEqual(french_to_english(''),'')

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Welcome'), 'Bienvenue')
        self.assertEqual(english_to_french(''), '')

unittest.main()