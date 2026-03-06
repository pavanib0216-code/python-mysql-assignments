# import csv

# with open('./data/courses.csv') as csv_file:


#     csv_reader = csv.reader(csv_file)
#     print(csv_reader) 

#     for line in csv_reader:
#         print(line)



with open('courses.txt', mode='r+') as csv_file:
    for line in csv_file.readlines():
        c_id, c_name, instructor = line.strip().split(',')
        print(f'{c_id}\t{c_name}\t{instructor}')  # we can format the output
