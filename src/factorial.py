"""
Factorial Calculator

Author: @RinchalShete
"""

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    n : int
        The number whose factorial is to be calculated.
        Must be a non-negative integer.

    Returns
    -------
    int
        Factorial of the given number.

    Raises
    ------
    TypeError
        If input is not an integer.
    ValueError
        If input is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
