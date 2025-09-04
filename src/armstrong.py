"""
Armstrong Checker

Author: Samridh Ramesha
"""

def armstrongChecker(num):
    """
    Checks if the number is an armstrong number or not

    Parameters:
    A non-negative integer -> num

    Returns:
    Boolean :- True if the integer is an armstrong number otherwise False

    """

    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num < 0:
        raise ValueError("Input must be a non-negative integer")

    digits = str(num)
    n = len(digits)  # number of digits

    total = sum(int(digit) ** n for digit in digits)
    return total == num
