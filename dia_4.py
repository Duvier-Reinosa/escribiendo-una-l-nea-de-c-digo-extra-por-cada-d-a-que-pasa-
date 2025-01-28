import requests
data = requests.get('https://rickandmortyapi.com/api/character').json()['results']
character = next((c for c in data if c['id'] == int(input("Digite el Id del personaje que estás buscando: "))), None)
print(f"ID: {character['id']}, Name: {character['name']}") if character else print("Personaje no encontrado")