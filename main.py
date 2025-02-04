"""
Main application.
"""

import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from math import sqrt

# create the Flask application
app = Flask(__name__)
# enable CORS for all routes
CORS(app)


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


@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    """
    Classify a given number.
    """
    # Get the number from query parameters
    number = request.args.get("number")

    if number is None:
        return jsonify({"number": "alphabet", "error": True}), 400

    try:
        number = int(number)
    except ValueError:
        return jsonify({"number": "alphabet", "error": True}), 400

    url = f"http://numbersapi.com/{number}/math"
    res = requests.get(url, timeout=0.5)
    fun_fact = res.text if res.status_code == 200 else "No fun fact available"

    props = ["armstrong"] if is_armstrong(number) else []
    props.append(is_even_or_odd(number))

    # Generate results
    results = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": props,
        "digit_sum": sum_digits(number),
        "fun_fact": fun_fact,
    }

    return jsonify(results), 200


# run the Flask application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
