import unittest
from src.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci("hello")

if __name__ == "__main__":
    unittest.main()
