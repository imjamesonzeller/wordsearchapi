import requests

url = 'http://api.jamesonzeller.com/generate_word_search'

words = ["PYTHON", "FLASK", "WEB", "SEARCH", "CODE"]

data = { 'words': words }

postResponse = requests.post(url, json=data)

if postResponse.status_code == 200:
    print("Word search generated successfully!")
    print(postResponse.json())
    for row in postResponse.json()['search']:
        print(" ".join(row))
    print(" ".join(postResponse.json()['words']))
else:
    print(f"Error: {postResponse.status_code}")
    print(postResponse.text)

getResponse = requests.get(url)
if getResponse.status_code == 200:
    print("Word search generated successfully!")
    print(getResponse.json())
    for row in getResponse.json()['search']:
        print(" ".join(row))
    print(" ".join(getResponse.json()['words']))
else:
    print(f"Error: {getResponse.status_code}")
    print(getResponse.text)