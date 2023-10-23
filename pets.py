import json

pets = [
    {"id": 1, "name": "Fido", "species": "Dog"},
    {"id": 2, "name": "Whiskers", "species": "Cat"},
    {"id": 3, "name": "Rover", "species": "Dog"},
]

def get_pets():
    return json.dumps(pets), 200
