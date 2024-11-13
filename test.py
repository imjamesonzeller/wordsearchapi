import requests

url = 'http://127.0.0.1:5000/generate_word_search'

words = ["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]

data = {}

response = requests.post(url)

if response.status_code == 200:
    print("Word search generated successfully!")
    print(response.json())
    for row in response.json()['search']:
        print(" ".join(row))
    print(" ".join(response.json()['words']))
else:
    print(f"Error: {response.status_code}")
    print(response.text)