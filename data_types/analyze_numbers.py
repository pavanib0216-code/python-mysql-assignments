import random

# Todo 1 - Generate 100 random integers
for i in range(100):
    num = random.randint(1. 100)
    random_num_list.append(num)

print(len(random_num_list))
print(randon_num_list)



# To-DO calculate avg of those integers
total_sum = 0

for num in random_num_list:
    total_sum += num 

print('\nCALCULATED TOTAL: ', total_sum)

average = total_sum / len(random_num_list)
print("\nCALCULATED AVERAGE: ", average)


#TO-DO 3: Find out how many integers are above the average
int_above_average = 0

for num in random_num_list:
    if num > average:
        ints_above_average += 1

print('INTS ABOVE AVERAGE: ', ints_above_average)

