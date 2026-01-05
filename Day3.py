# Typecasting

# Typecasting the process of changing one data type to another.
# data_Type()

# int --> str
# str(12) --> "12"

# First way
# num = 12
# print('raunak'+str(num))

# Second way
# num = 12
# num = str(num)
# print('raunak'+num)

# Third way
# num = str(12)
# print('raunak'+num)

# float --> str
# str(3.12) --> "3.12"
# num = 3.12
# print('Raunak'+str(num))

# bool --> str
# str(True) --> "True"
# b = True
# print('raunak'+str(b))

# str --> int
# int("12") --> 12
# int("ab") --> X (This will give us error)

# num = "12"
# num1 = "13"
# print(int(num) + int(num1))

# float --> int
# int(1.02) --> 1
# the decimal values get discarded
# num = 1.02
# print(int(num))

# bool --> int
# True --> 1
# False --> 0
# b = True
# print(int(b) + int(b))

# int --> float
# print(float(3))

# str --> float
# print(float("3.32"))

# str --> bool
# empty string ('') = False

# print(bool("gautam")) # --> True as this is not an empty string
# print(bool("")) # --> False as the string is empty

# int --> bool
# only 0 = False

# print(bool(2))

# float --> bool
# only 0.0 = False
# print(bool(0.00))

# input()

# in python, we take inputs from users through terminal using the --> input() function

# input("Enter something")
#               ^
#               |
#    message that will be displayed in the terminal

# First
# num = int(input("Enter something : "))
# print(num+num)

# Second
# num = input("Enter something : ")
# print(int(num)+int(num))

# Task : Take first_name and last_name as input and concatenate them

# first_name = input("Enter first name : ")
# last_name = input("Enter last name : ")

# print(f'{first_name} {last_name}')


# simple calculator
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(f'sum is {num1+num2}')
print(f'difference is {num1 - num2}')
print(f'multiplication is {num1*num2}')
print(f'division is {num1/num2}')

# Task take first name and last as user input and display their first character and last character with the summation of their length.



