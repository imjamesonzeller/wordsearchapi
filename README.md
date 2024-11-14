# Word Search API

This project provides a simple API to generate word search grids based on a list of words. It uses Flask as the web framework and allows users to send a list of words via a POST request to generate a word search grid. The API returns a JSON object representing the grid and the words that are contained.

## Features

- **Word Search Generation**: Send a list of words to the API, and it will return a grid with the words placed in random locations along with words that are contained.
- **POST Method**: Accepts `POST` requests containing a JSON object with a list of words.
- **JSON Response**: Returns a JSON object representing the generated word search grid along with the words that are contained.

## Requirements

- Python 3.x
- Flask
- `requests` (for testing)
- `flask_cors` (for enabling CORS)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/imjamesonzeller/wordsearchapi.git
cd word-search-api
```

### 2. Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, install Flask and CORS manually:

```bash
pip install Flask flask_cors
```

### 3. Run the Flask API Server

Start the Flask server by running the following command:

```bash
python app.py
```

By default, the API will be available at `http://localhost:5000`. If you want to deploy it to a different IP or port, you can modify the `app.run()` call in `app.py`.

## WordSearch Class

The core of the word search generator is the `WordSearch` class, which takes a list of words and generates a grid that places each word randomly within the grid. 

### Class: `WordSearch`

#### Methods:

- **`__init__(self, words)`**  
  Initializes the `WordSearch` object with a list of words and sets up the grid. The grid size is computed based on the number of words and the length of the words. It ensures that only words of valid lengths are placed on the grid.

- **`__computeGridSize(self)`**  
  Calculates an appropriate size for the word search grid based on the number of words and their average lengths. It ensures that the grid is large enough to fit the words in a random pattern.

- **`__randomCoords(self)`**  
  Returns a tuple of random coordinates within the grid.

- **`__valid_direction(self, word, coords)`**  
  Checks if a word can be placed at the given coordinates in any of the 8 possible directions (horizontal, vertical, diagonal). This method also verifies that the word fits within the grid and that it doesn't overlap with existing words incorrectly.

- **`__place_word(self, word, coords, direction)`**  
  Places the word at the given coordinates in the grid, following the chosen direction.

- **`__fillBlankIn(self)`**  
  Fills in all the remaining empty spaces in the grid with random letters.

- **`generate_word_search(self)`**  
  The main method that generates the word search. It iterates through the list of words, places each word randomly on the grid, and then fills in the blank spaces with random letters.

- **Word Length Validation**: During word placement, the code ensures that each word is properly placed without exceeding the grid size or overlapping with other words incorrectly. The grid size is automatically adjusted to accommodate the longest word in the list.

### Example of Grid Generation

Here’s an example of how the `generate_word_search()` method works:

1. **Input**: A list of words, e.g., `["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]`.
2. **Output**: A grid with those words placed randomly in 8 possible directions, with remaining empty spaces filled with random letters.

Example grid before random letter insertion:

```json
[
  ["P", "Y", "T", "H", "O", "N", "", "", "", ""],
  ["", "", "", "", "", "", "", "", "", ""],
  ["", "", "", "", "", "B", "E", "W", "", ""],
  ["", "F", "", "", "", "S", "", "", "", ""],
  ["", "", "L", "", "E", "", "", "", "", ""],
  ["", "", "", "A", "", "", "", "", "", ""],
  ["", "", "R", "", "S", "", "", "", "", "C"],
  ["", "C", "", "", "", "K", "", "", "", "O"],
  ["H", "", "", "", "", "", "", "", "", "D"],
  ["", "", "", "", "", "", "", "", "", "E"]
]
```

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
{
  "search": [
    ["P", "Y", "T", "H", "O", "N", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "B", "E", "W", "", ""],
    ["", "F", "", "", "", "S", "", "", "", ""],
    ["", "", "L", "", "E", "", "", "", "", ""],
    ["", "", "", "A", "", "", "", "", "", ""],
    ["", "", "R", "", "S", "", "", "", "", "C"],
    ["", "C", "", "", "", "K", "", "", "", "O"],
    ["H", "", "", "", "", "", "", "", "", "D"],
    ["", "", "", "", "", "", "", "", "", "E"]
  ],
  "words": ["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]
}
```

#### Error Responses

- **400 Bad Request**: If an invalid request is sent (e.g., missing words), the server responds with a default list of  15 randomly selected words and generates the grid.

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

If successful, you'll receive a JSON response with the generated word search grid and contained words.

### Example Python Test Script

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

The test.py file also works well with better formating for CLI word searches.

### Dependencies for Testing

If you're testing the API using Python, you'll need to install the `requests` library:

```bash
pip install requests
```

## Code Explanation

### `app.py`

The Flask API is defined in `app.py`. The key parts of the code are:

- **CORS**: This is enabled to allow cross-origin requests, which is particularly useful if you're hosting the API and front-end on different domains.
  
- **POST `/generate_word_search`**: The main endpoint where users can send a list of words. If no words are provided, a default list of random words from words.py will be used. The `WordSearch` class is used to generate the word search grid.

- **Error Handling**: If an invalid request is sent (e.g., missing words), the server responds with a default list of words and generates the grid.

# Self-Hosting & Deployment

This Word Search API is self-hosted on my home server using Docker. The API is publicly accessible at the following URL:

- **API Endpoint**: [https://wordsearch.jamesonzeller.com/generate_word_search](https://wordsearch.jamesonzeller.com/generate_word_search)

### Hosting with Docker

To make the API publicly available, I’ve containerized the application using Docker. 
## Website Integration

To make the word search functionality easily accessible from my website, I’ve integrated the API into my site. Users can generate word search grids directly through the following URL:

- **Word Search on Website**: [https://www.jamesonzeller.com/wordsearch](https://www.jamesonzeller.com/wordsearch)

On this page, I created a user-friendly interface where visitors can input their own words, and the backend API will generate a custom word search grid. The integration uses JavaScript to send a POST request to the API, retrieve the word search grid, and display it dynamically on the page.

### Example Website Flow

1. **User Input**: The user enters a list of words they’d like to see in the word search along with a delimiter that seperates their words.
2. **API Request**: The JavaScript frontend sends a POST request to the API (`https://wordsearch.jamesonzeller.com/generate_word_search`) with the words provided by the user.
3. **Grid Generation**: The API processes the request, generates the word search grid, and returns the result as a JSON response.
4. **Display**: The website displays the generated grid in an interactive format, where the user can see the words arranged in the grid.
5. **Download**: The JavaScript frontend processes the JSON response and creates a CSV file and displays the download link to provide easy printing.

### Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Containerization**: Docker
- **Hosting**: Home server with Cloudflare Tunnel
- **CORS**: Enabled for cross-origin requests from the website to the API

## Conclusion

The Word Search API is a fun and simple tool to generate word search grids. By self-hosting it on my home server and integrating it into my website, I’ve made it accessible to anyone who wants to create their own word search puzzles. This project demonstrates my ability to work with both backend and frontend technologies, as well as my familiarity with Docker and cloud-based hosting.

Feel free to try it out on the website or directly interact with the API at the provided endpoints!

## License

This project is open source and available under the MIT License.
