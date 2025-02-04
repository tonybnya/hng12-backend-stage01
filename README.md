# Stage 1 Backend - Number Classification API

**Task**:
Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Description

## Setup and installation

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
curl http://localhost:5000/
```

Using JavaScript `fetch`:

```javascript
fetch('http://localhost:5000/')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Technologies Used

- Python3
- Flask
- Flask-CORS

## Additional Information

If you're looking for experienced Python developers, you can find and hire elite Python developers here: [HNG Tech Python Developers](https://hng.tech/hire/python-developers).
