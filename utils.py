"""
Utility functions.
"""
from math import sqrt


def is_armstrong(n: int) -> bool:
    """
    Check if a number is armstrong or not.
    """
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))


def is_even_or_odd(n: int) -> str:
    """
    Check if a number is even or odd.
    """
    return 'even' if n % 2 == 0 else 'odd'



def is_prime(n: int) -> bool:
    """
    Check if a number is a prime or not.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % i != 0 for i in range(5, int(sqrt(n)) + 1, 2))


def is_perfect(n: int) -> bool:
    """
    Check if a number is perfect or not.
    """
    if n < 2:
        return False

    sum_divisors = sum(i + (n // i) for i in range(2, int(sqrt(n)) + 1) if n % i == 0)

    return sum_divisors == n


def sum_digits(n: int) -> int:
    """
    Sum all digits.
    """
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


if __name__ == '__main__':
    print(is_prime(11))
    print(is_prime(1))
    print(is_prime(13))
