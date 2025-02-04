"""
Utility functions.
"""

from math import sqrt


def is_armstrong(n: int) -> bool:
    """
    Check if a number is armstrong or not.
    """
    num = abs(n)
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))


def is_even_or_odd(n: int) -> str:
    """
    Check if a number is even or odd.
    """
    return "even" if abs(n) % 2 == 0 else "odd"


def is_prime(n: int) -> bool:
    """
    Check if a number is a prime or not.
    """
    if abs(n) < 2:
        return False
    num = abs(n)
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    return all(num % i != 0 for i in range(5, int(sqrt(num)) + 1, 2))


def is_perfect(n: int) -> bool:
    """
    Check if a number is perfect or not.
    """
    num = abs(n)
    if num < 2:
        return False

    sum_divisors = sum(
        i + (num // i) for i in range(2, int(sqrt(num)) + 1) if num % i == 0
    )

    return sum_divisors == num


def sum_digits(n: int) -> int:
    """
    Sum all digits.
    """
    try:
        num = abs(n)
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return -total if str(n).startswith("-") else total
    except ValueError:
        raise ValueError("Invalid number format")
