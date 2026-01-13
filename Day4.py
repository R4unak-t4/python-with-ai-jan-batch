# comparison operators

# > (greater than operator)
# print(5 > 4)

# < (less than operator)
# print(4 < 5)

# >= (greater than or equal to operator)
# print(4 >= 4)

# <= (less than or equal to operator)
# print(5 <= 6)

# != not equals
# print(5 != 4)

# ==
# print(5 == 5)

# Logical operator

# and (*)

# print(True * True)
#       1  X  1 --> 1
# print(True * False)
#       1  X  0 --> 0

# print(True and True)

# print(False and False)

# or (+)
# print(bool(True + True))
#       1  +  1 --> 2 --> bool(2) --> True
# print(bool(True + False))
#       1  +  0 --> 1 --> bool(1) --> True


# print(False or False)
#       0    +   0 --> 0


'''
True and True and False --> False
True and False or True --> True
True and False and False --> False
False or True or False --> True
'''

# print(True and True and False)
# print(False or True or False)

# conditional statements

# if (condition), the condition must always give boolean values
# num = 5
# if num > 4 :
#     print('hello')
# elif num > 1:
#     print('hello elif')
# elif num >3 :
#     print('hello gautam')
# else:
#     print('else hello')

# TASK : make a calculator

# take 2 numbers as input from user
# take operator as input from user
# according the operator perform the arithmetic operation : (+,-,*,/)

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
operator = input('Enter operator')

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print('invalid operator')