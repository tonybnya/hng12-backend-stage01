# Stage 1 Backend - Number Classification API

**Task**:
Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Description

From a query parameter, this API provides some interesting informations about a number:

- if it's a prime or not
- if it's perfect or not
- if it's a armstrong number or not
- if it's an even or an odd number
- the sum of its digits
- a fun fact about this number

## Setup and installation

1. Clone the repository:

```bash
git clone https://github.com/tonybnya/hng12-backend-stage01.git
cd hng12-backend-stage01
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip3 install -r requirements.txt
```

4. Run the application:

```bash
python3 main.py
```

## API Documentation

**Endpoint**:

- Development URL: ``http://localhost:5000/
- Production URL: ``
- Method: `GET** <your-domain.com>/api/classify-number?number=371`
- CORS: Enabled for all origins

**Response Format**:

- Required JSON Response Format (200 OK):

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
}
```

- Required JSON Response Format (400 Bad Request)

```json
{
    "number": "alphabet",
    "error": true
}
```

**Example Usage**:

Using `curl`:

```bash
curl http://localhost:5000/api/classify-number?number=371
```

Using JavaScript `fetch`:

```javascript
fetch('http://localhost:5000/api/classify-number?number=371')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Technologies Used

- Python3
- Flask
- Flask-CORS

## Additional Information

If you're looking for experienced Python developers, you can find and hire elite Python developers here: [HNG Tech Python Developers](https://hng.tech/hire/python-developers).
