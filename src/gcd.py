def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.

    Parameters:
        a (int): first number
        b (int): second number

    Returns:
        int: GCD of a and b

    Author: @SOUMYA122004
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    a, b = abs(a), abs(b)  # <-- convert to positive
    while b:
        a, b = b, a % b
    return a