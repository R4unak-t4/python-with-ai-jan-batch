# Arithmetic Operations

# +, -, *, /, %

# Can only be performed on numeric data types

# addition ( + ) :
# num1 = 1
# num2 = 3
# print(num1 + num2)

# difference ( - ) :
# num1 = 1
# num2 = 3
# print(num1 - num2)

# multiplication ( * ) :
# num1 = 2
# num2 = 3
# print(num1 * num2)

# division ( / ) :
# num1 = 50
# num2 = 2
# print(num1/num2)

# modulo ( % ) :
# num1 = 13
# num2 = 2
# print(num1 % num2)

# Task perform +, -, *, / and % on float :

# addition ( + ) :
# num1 = 1.04
# num2 = 3.67
# print(num1 + num2)

# difference ( - ) :
# num1 = 1.03
# num2 = 3.04
# print(num1 - num2)

# string operations

# enclosed in quotation marks " ".

# '', ""
# name = 'raunak'
# name = "raunak"

# """ """, ''' '''
# sentence = '''hello
# how are you
# I am fine
# '''

# Indexing in strings

# P Y T H O N
# 0 1 2 3 4 5
# index starts from 0
# index ends at n - 1, where n is the total number of characters in string

# len() --> return the length of the string, number of characters in string

# print(len('python'))

# accessing characters with index

word = 'python'
# we use square brackets : [], to access with help of index

# variable_name[index]
'''
since the variable word holds the string 'Python'
and we entered 0 for the index value --> word[0]
we will get the first letter of the word python
which is 'p', since the letter 'p' is indexed 0
'''
# print(word[2])

# since the index 6 does not exist in the string 'python' as it's maximum value for index is 5, we will get string 'index out of range' error
# print(word[6])

# Task : Find the length of your first name and access the first letter and last letter of your name using index.

# first_name = 'Raunak'
# print(len(first_name))
# print(first_name[0])
# print(first_name[len(first_name) - 1])

# string concatenation

# we use '+' operator to concatenate  strings

# word1 = 'hello'
# word2 = 'world'
#
# print(word1 +" "+ word2)

# Task : concatenate your first name with your last name with a space in between.

# first_name = 'Raunak'
# last_name = 'Thapa'
#
# print(first_name + " " + last_name)

# .replace()
# print("banana".replace('a','o'))



