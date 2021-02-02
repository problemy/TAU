import requests
import json
#use pytest
url = 'https://pokeapi.co/api/v2/pokemon'

response = requests.request("GET", url)

def test_api_connection():
    assert response.status_code == 200

def test_bad_request():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/1119")
    assert response.status_code == 404

def test_keys():
        expected = ["count", "next", "previous","results"]
        current = []
        a = json.loads(response.text)
        for k in a:
            if k in expected:
                current.append(k)
        assert expected == current

def test_values():
        test_pokemon_url = "https://pokeapi.co/api/v2/pokemon/1/"
        response = requests.get(test_pokemon_url)
        expected_pokemon_name = "bulbasaur"
        current = ""
        a = json.loads(response.text)
        for key, value in a.items():
            print(key, value)
            if key == "name":
                 current = value
        #print(current)
        assert expected_pokemon_name == current

