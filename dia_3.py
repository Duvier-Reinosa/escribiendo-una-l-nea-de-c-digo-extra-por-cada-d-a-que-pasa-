import requests
response = requests.get('https://rickandmortyapi.com/api/character')
for character in response.json()['results'][:10]: print(f"ID: {character['id']}, Name: {character['name']}")