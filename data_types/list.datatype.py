# mylist=[] # create a empty list
# print(mylist)
# # Create a list of strings.
# string_list = ["Hello", "Python", "World"]
# print(string_list)
# # Create a list of numbers.
# number_list = [3, 4, 5, 6, 8, 10]
# print(number_list)
# # Create a list of boolean values.
# boolean_list = [True, False, False, True]
# print(boolean_list)
# # Create a mixed list or list with heterogeneous data
# mixed_list = [3, 4, "Python", True]
# print(mixed_list) 

print('============= List Methods==============\n')

# Create a empty list
my_list = []

# Add a new element to the list
my_list.append(1) # [1]
my_list.append(2) # [1,2]
my_list.append(3) # [1,2,3]

print(my_list)

mylist = []
print(mylist)

string_list = ["Hello", "Python", "World"]
print(string_list)

number_list = [3, 4, 5, 6, 8, 10]
print(number_list)

boolean_list = [True, False, False, True]
print(boolean_list)

mixed_list = [3, 4, "Python", True]
print(mixed_list) 


=====Access list elements====
names = ["Jeff", "Bill", "Steve", "Mohan"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
# print(names[4])  # IndexError


======Convert string → list======
my_string = "Hello World"

character_list = list(my_string)
substring_list = my_string.split()

print(my_string)
print(character_list)
print(substring_list) 



=====Modify list elements======
my_list = [1, 2, 3, 4, 5]
print("before:", my_list)

my_list[2] = 7
print("after:", my_list)

my_list = [1, "Hello Python", 7.98]
print("before: ", my_list[1])

my_list[1] = "Hello JavaScript"
print("after: ", my_list[1]) 


===append()====
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)


====extend()====
my_list = []
my_list.extend([1, 2, 3])

print(my_list) 


====insert()====
my_list = [1, 2, 4, 5]
my_list.insert(2, 3)

print(my_list) 


====remove()====
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)

print(my_list) 


====sort()====
my_list = [5, 2, 6, 4, 1, 1, 3]
my_list.sort()

print(my_list) 



====concatenate lists====
list1 = [1, 2, 3]
list2 = [4, 5, 6]

new_list = list1 + list2
print(new_list) 



====traverse lists====
my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

for i in range(len(my_list)):
    print(f"Index {i} contains: {my_list[i]}") 



===random list===
import random

values = []
for i in range(5):
    values.append(random.randint(1, 100))

print(values) 


====nested list====
my_list = [[1,2,3],[4,5,6],[7,8,9]]
print(my_list[1][1]) 


====nested list example===
nested_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ['apple','banana','orange']
] 


====nested iteration===
my_list = [[1,2,3],[4,5,6],[7,8,9]]

for sublist in my_list:
    for element in sublist:
        print(element) 



====deep nested access===
nums = [1,2,3,[4,5,6,[7,8,[9]]],10]

print(nums[0])
print(nums[1])
print(nums[3])
print(nums[4])
print(nums[3][0])
print(nums[3][3])
print(nums[3][3][0])
print(nums[3][3][2]) 


====Section 3 — Dictionaries====
▶️ create dictionary
my_dictionary = {
    "first": "John",
    "last": "Doe",
    "city": "New York",
    "year": 2023,
    "average": 100
}

print(my_dictionary["first"])
print(my_dictionary["year"]) 


===dict constructor====
car = dict(brand='Toyota', model='Camry', year=2022)

print(car["brand"])
print(car["model"])
print(car["year"])    


====dictionary from lists===
keys = ['a','b','c']
values = ["A for Apple","B for banana","C for Cat"]

my_dict = dict(zip(keys,values))

print(my_dict["a"])
print(my_dict["b"])
print(my_dict["c"])  


