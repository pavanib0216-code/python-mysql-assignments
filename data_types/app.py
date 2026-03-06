file = open('./data/my_file.txt', encoding='cp1252')

with open('./data/my_file.txt', encoding='cp1252') as file:
    print(file.name)
    print(file.mode)
    print(file.encoding)
    print(file.read())

# Using the same file created from previous section
with open('./data/my_file.txt', mode = 'r+') as fo:
  print(fo.read(3)) # prints 'How'
  print(fo.tell())  # prints '3'
  fo.seek(45)    # moves the cursor from 3 to 45
  print(fo.tell()) # prints '45'
  print(fo.read()) # prints 'This is currently the last line\n'



def write_names_to_file(names, file_path):
    try:
        with open(file_path, 'w') as fp:
            for item in names:
                # fp.write("%s\n" % item)
                fp.write(f"{item}\n")
                print(item)
            print('Names have been written to the file.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example of using the function
names = ['Jessa', 'Eric', 'Bob']

#file_path = r'E:/files_Path/sales.txt'
file_path = r'sales.txt'

write_names_to_file(names, file_path)py