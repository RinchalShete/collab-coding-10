import os
import sys
import unittest

# Ensure repo root is on sys.path so "src" can be imported during discovery
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.is_even import is_even

class TestIsEven(unittest.TestCase):
    def test_is_even_true(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))

    def test_is_even_false(self):
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-5))

if __name__ == "__main__":
    unittest.main()
