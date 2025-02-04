"""
Main application.
"""

import httpx
import os
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
        "task": "Number Classification API",
    }
    return jsonify(data), 200


async def get_fun_fact(number):
    """
    Get a fun fact about a number.
    """
    url = f"http://numbersapi.com/{number}/math"
    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url, timeout=0.5)
            return res.text if res.status_code == 200 else "No fun fact available"
        except httpx.RequestError:
            return "No fun fact available"


@app.route("/api/classify-number", methods=["GET"])
async def classify_number():
    """
    Classify a given number.
    """
    # Get the number from query parameters
    number = request.args.get("number")

    # if number is None:
    #     return jsonify({"number": "alphabet", "error": True}), 400

    try:
        number = int(number)
    except ValueError:
        return jsonify({"number": "alphabet", "error": True}), 400

    fun_fact = await get_fun_fact(number)

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
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port)
