import requests

response = requests.get('https://official-joke-api.appspot.com/random_joke')
if response.status_code == 200:
    joke = response.json()
    print(f"{joke['setup']}\n{joke['punchline']}")
else:
    print('Failed to fetch a joke.')