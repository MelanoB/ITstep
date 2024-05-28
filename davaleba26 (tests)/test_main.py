import unittest
from main import *


class Test(unittest.TestCase):
    def test_reverse_str(self):
        self.assertEqual(reverse_str("hello"), "olleh")
        self.assertEqual(reverse_str(""), "")
        self.assertEqual(reverse_str("!@#"), "#@!")
        self.assertNotEqual(reverse_str("World"), "drowl")

    def test_palindrome(self):
        self.assertTrue(palindrome("madam"))
        self.assertFalse(palindrome("hello"))
        self.assertTrue(palindrome(""))

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("mY naMe iS"), "My Name Is")
        self.assertNotEqual(capitalize_words("testing, checking"), "TESTING, CHECKING")

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertNotEqual(celsius_to_fahrenheit(10), 20)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(-40), -40)
        self.assertEqual(fahrenheit_to_celsius(392), 200)
        self.assertNotEqual(fahrenheit_to_celsius(-5), 100)
