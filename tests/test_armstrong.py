# This is for testing Armstrong number function.
import unittest
from src.armstrong import armstrongChecker

class TestArmstrong(unittest.TestCase):

    def test_single_digit_numbers(self):
        # All single-digit numbers are Armstrong
        for i in range(10):
            self.assertTrue(armstrongChecker(i))

    def test_known_armstrong_numbers(self):
        self.assertTrue(armstrongChecker(153))
        self.assertTrue(armstrongChecker(9474))
        self.assertTrue(armstrongChecker(370))
        self.assertTrue(armstrongChecker(407))

    def test_non_armstrong_numbers(self):
        self.assertFalse(armstrongChecker(123))
        self.assertFalse(armstrongChecker(200))
        self.assertFalse(armstrongChecker(9475))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            armstrongChecker(-153)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            armstrongChecker(12.5)
        with self.assertRaises(TypeError):
            armstrongChecker("153")
        with self.assertRaises(TypeError):
            armstrongChecker([1, 5, 3])

if __name__ == "__main__":
    unittest.main()
