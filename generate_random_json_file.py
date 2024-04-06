import json
import random
import string

def generate_random_json(file_name, num_objects):
    data = []
    for _ in range(num_objects):
        obj = {
            'name': ''.join(random.choices(string.ascii_letters, k=5)), 
            'age': random.randint(18, 80),  
            'city': random.choice(['Aba', 'Calabar', 'Port Harcourt', 'Ibadan', 'Uyo'])  
        }
        data.append(obj)

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return file_name

