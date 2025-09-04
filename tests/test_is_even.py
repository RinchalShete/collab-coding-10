import pytest
from src.is_even import is_even

def test_is_even_true():
    assert is_even(2)
    assert is_even(0)
    assert is_even(-4)

def test_is_even_false():
    assert not is_even(3)
    assert not is_even(-5)

if __name__ == "__main__":
    pytest.main()
