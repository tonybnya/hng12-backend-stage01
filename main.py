"""
Main application.
"""
import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import is_armstrong, is_even_or_odd, is_perfect, is_prime, sum_digits

# create the Flask application
app = Flask(__name__)
# enable CORS for all routes
CORS(app)


# define the root endpoint
@app.route("/")
def home():
    """
    Root endpoint.
    """
    data = {
        "from": "HNG Internship 12",
        "track": "Backend",
        "stage": 1,
        "task": "Number Classification API"
    }
    return jsonify(data), 200


@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    """
    Classify a given number.
    """
    # Get the number from query parameters
    number = request.args.get("number")

    if number is None:
        return jsonify(
            {
                "number": "alphabet",
                "error": True
            }
        ), 400

    try:
        number = int(number)
    except ValueError:
        return jsonify(
            {
                "number": "alphabet",
                "error": True
            }
        ), 400

    url = f"http://numbersapi.com/{number}/math"

    try:
        res = requests.get(url, timeout=0.5)
        fun_fact: str = res.text
    except requests.exceptions.Timeout:
        return jsonify(
            {
                "number": "alphabet",
                "error": True
            }
        ), 400
    except requests.exceptions.RequestException:
        return jsonify(
            {
                "number": "alphabet",
                "error": True
            }
        ), 400

    props = []
    if is_armstrong(number):
        props.append('armstrong')

    props.append(is_even_or_odd(number))

    # Generate results
    results = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": props,
        "digit_sum": sum_digits(number),
        "fun_fact": fun_fact
    }

    return jsonify(results), 200


# run the Flask application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port)
