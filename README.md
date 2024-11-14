# Word Search API

This project provides a simple API to generate word search grids based on a list of words. It uses Flask as the web framework and allows users to send a list of words via a POST request to generate a word search grid. The API returns a JSON object representing the grid.

## Features

- **Word Search Generation**: Send a list of words to the API, and it will return a grid with the words placed in random locations.
- **POST Method**: Accepts `POST` requests containing a JSON object with a list of words.
- **JSON Response**: Returns a JSON object representing the generated word search grid.

## Requirements

- Python 3.x
- Flask
- `requests` (for testing)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/word-search-api.git
cd word-search-api
```

### 2. Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, install Flask manually:

```bash
pip install Flask
```

### 3. Run the Flask API Server

Start the Flask server by running the following command:

```bash
python app.py
```

By default, the API will be available at `http://localhost:5000`. If you want to deploy it to a different IP or port, you can modify the `app.run()` call in `app.py`.

## API Endpoints

### `POST /generate_word_search`

This endpoint accepts a list of words and returns a generated word search grid in a JSON format.

#### Request

- **URL**: `/generate_word_search`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Request Body**: A JSON object with a key `words` containing a list of words.

Example request body:

```json
{
  "words": ["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]
}
```

#### Response

The response will be a JSON object representing the word search grid.

Example response:

```json
[
  ["P", "Y", "T", "H", "O", "N", "", "", "", ""],
  ["", "", "", "", "", "F", "L", "A", "S", "K"],
  ["", "", "", "", "", "W", "E", "B", "", ""],
  ["", "", "", "", "", "", "S", "E", "A", "R"],
  ["", "", "", "", "", "", "", "", "C", "O"],
  ["", "", "", "", "", "", "", "", "D", "E"],
  ["", "", "", "", "", "", "", "", "", "C"],
  ["", "", "", "", "", "", "", "", "", "O"],
  ["", "", "", "", "", "", "", "", "", "D"],
  ["", "", "", "", "", "", "", "", "", "E"]
]
```

Each letter in the grid represents a position in the word search, and empty strings (`""`) are places where no word is placed.

#### Error Responses

- **400 Bad Request**: If no words are provided or if the request body is malformed, the API will return an error message.

Example:

```json
{
  "error": "No words provided"
}
```

- **404 Not Found**: If the endpoint is incorrect or unavailable.
  
- **500 Internal Server Error**: If there is a server-side error.

## Testing the API

You can test the API using a tool like **Postman** or **cURL**. Here's how to do it with **cURL**:

### Example cURL Request:

```bash
curl -X POST http://localhost:5000/generate_word_search \
     -H "Content-Type: application/json" \
     -d '{"words": ["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]}'
```

If successful, you'll receive a JSON response with the generated word search grid.

## Example Python Test Script

You can also test the API with the following Python script using the `requests` library:

```python
import requests
import json

# URL of your Flask API endpoint
url = 'http://localhost:5000/generate_word_search'

# Example list of words
words = ["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]

# Data to send in the POST request body
data = {
    "words": words
}

# Send the POST request to the Flask API
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the generated word search grid (JSON response)
    print("Word search generated successfully!")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

### Dependencies for Testing

If you're testing the API using Python, you'll need to install the `requests` library:

```bash
pip install requests
```

## Notes

- The word search generation logic is currently a basic example. It places words horizontally, and it doesn't account for word overlap or filling empty spaces with random letters.
- You can modify the `generate_word_search` function in `app.py` to implement more complex word placement algorithms.
- The API does not currently validate the size of the word search grid. If you send too many long words, the grid might overflow. You can implement constraints for grid size and word length as needed.

## License

This project is open source and available under the MIT License.
