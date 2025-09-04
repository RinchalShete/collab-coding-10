"""
Even Number Checker

Author: @TheBlueGeneral
"""

def is_even(n: int) -> bool:
    """
    Check whether a given integer is even.

    Parameters
    ----------
    n : int
        The integer to check.

    Returns
    -------
    bool
        True if n is even, False otherwise.

    Raises
    ------
    TypeError
        If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("is_even is only defined for integers.")
    return n % 2 == 0
