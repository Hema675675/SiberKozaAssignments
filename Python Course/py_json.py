# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON_iy = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user_iy = json.loads(userJSON_iy)

# print(user)
# print(user['first_name'])

car_iy = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_iy = json.dumps(car_iy)

print(carJSON_iy)
