def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)