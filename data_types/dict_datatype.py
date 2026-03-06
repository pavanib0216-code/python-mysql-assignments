# Create a dictionary to store learner information.
my_dictionary = {
    "first": "John",
    "last": "Doe",
    "city": "New York",
    "year": 2023,
    "average": 100
}
# Access values in the dictionary.
print(my_dictionary["first"])  # Output: John
print(my_dictionary["year"])   # Output: 2023 

###The dict() constructor can be used to create a dictionary.
car = dict(brand='Toyota', model='Camry', year=2022)

# Access values in the dictionary.
print(car["brand"])  # Output: Toyota
print(car["model"])  # Output: Camry
print(car["year"])  # Output: 2022 

#You can create a dictionary from two lists—one for keys
#and another for values.
keys = ['a', 'b', 'c']
values = ["A for Apple", "B for banana", "C for Cat"]
my_dict = dict(zip(keys, values))

# Access values in the dictionary.
print(my_dict["a"])
print(my_dict["b"])
print(my_dict["c"])

#Dict methods
print(my_dict.values())
print("ITEMS: ", my_dict.values())
print("ITEMS: ", my_dict.items())

electric_car = {
    "year": 2022,
}

electric_car['model'] = 'X'
electric_car['model'] = 'Tesla'

print(electric_car)