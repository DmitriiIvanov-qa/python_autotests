import requests

host = 'https://pokemonbattle.me:9104'
token = '4e22e163d77f56527da0554e14930b47'

answer_new_pokemon = requests.post(f'{host}/pokemons', json = 
                       {
    "name": "Yobbo",
    "photo": "https://dolnikov.ru/pokemons/albums/096.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})
print(answer_new_pokemon.status_code, answer_new_pokemon.text)

answer_new_name = requests.put(f'{host}/pokemons', json = 
                       {
    "pokemon_id": "10004",
    "name": "Yob",
    "photo": "https://dolnikov.ru/pokemons/albums/095.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})
print(answer_new_name.status_code, answer_new_name.text)

answer_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = 
                       {
    "pokemon_id": "10004"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})
print(answer_pokeball.status_code, answer_pokeball.text)