print('Hello World!')   

print('we can do this!') 

print(3 * 7)

def my_func(name):
    print(name)

# ===== Input Function ===============

# Ask for the user name
user_name = input("Enter your name: ") # store the name in a variable

print(user_name) # print the name to the terminal

# This is a comment
print('Hello World!')

# This is another comment
print('Hello Python!!!')

print(3 + 7)
# print(3 + 7)

def my_func(name):
    """
        Multiline comment / Doc String  
        This function print the argument name
        arg: name
    """
    print(name)
    
my_func("abe") # prints the name 'abe'

print('Company Acme INC', 20000, 'Feb', sep=' | ')

# ===== Input Function ===============

# Ask for the user name
user_name = input("Enter your name: ") # store the name in a variable

print('welcome: ', user_name) # print the name to the terminal 

user_mobile = input('enter your mobile number: ') 
print("mobile number: ", user_mobile)    

user_email = input("Enter your email: ")
print("User Email: ", user_email)

print(f'User Details: Name, {user_name} phone, {user_mobile} Email, {user_email}') 