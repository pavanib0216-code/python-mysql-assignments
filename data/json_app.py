import requests

url = "https://jsonplaceholder.typicode.com/users/1"

req =  requests.get(url)

print(req.text)

user_dict = req.json()

user_dict["level"] = 1
print(user_dict["name"]) 

import json 


import json

with open('./data/data.json') as json_file:
#Deserialize data from the file into Python dictionary object.
  data = json.load(json_file)
  data['isPresent'] = True
  
  print(data)


# Your object (e.g., a dictionary)
my_object = {
    "name": 'John',
    "age": 30,
    "city": "New York"
}

# Convert to JSON
json_string = json.dumps(my_object)

print(json_string)