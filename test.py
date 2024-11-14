import requests

url = 'http://wordsearch.jamesonzeller.com/generate_word_search'

words = ["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]

data = { 'words': words }

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Word search generated successfully!")
    print(response.json())
    for row in response.json()['search']:
        print(" ".join(row))
    print(" ".join(response.json()['words']))
else:
    print(f"Error: {response.status_code}")
    print(response.text)