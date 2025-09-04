import unittest
from src.gcd import gcd

class TestGCD(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(gcd(20, 30), 10)

    def test_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(gcd(-20, 30), 10)
        self.assertEqual(gcd(20, -30), 10)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            gcd(10, "a")

if __name__ == "__main__":
    unittest.main()