import unittest
from src.is_even import is_even

class TestIsEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(-4))

    def test_odd_numbers(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-7))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_even(3.5)
        with self.assertRaises(TypeError):
            is_even("10")

if __name__ == "__main__":
    unittest.main()
