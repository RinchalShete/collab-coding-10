import unittest
from src.factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_non_integer(self):
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("abc")
        with self.assertRaises(TypeError):
            factorial([1, 2, 3])

if __name__ == "__main__":
    unittest.main()
