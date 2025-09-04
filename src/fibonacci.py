def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Parameters:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Author: @shivateja126
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
