# tuple
# tuples are enclosed in small brackets : ()

# my_tuple = (1,2,3)
# getting values through index
# print(my_tuple[len(my_tuple) - 1])

# changing value
# my_tuple[1] = 12

# dictionary

# it stores data in key value pairs

# "key" : "value"

# dictionary is enclosed in curly braces {}

# my_dict = {
#     "key" : "value",
#     12 : 13,
#     15.6 : True,
#     True : "hello"
# }

# accessign the values in dictionary
# print(my_dict["key"])
# print(my_dict[12])

# replacing the value
# my_dict[12]  = "raunak"
# print(my_dict[12])

# adding new key
# my_dict['name'] = 'thapa'
# print(my_dict)

# info = {
#     'ID' : 1,
#     "name" : 'raunak',
#     "age" : 20,
#     "weight" : 64.23
# }
# print('ID' in info)
#
# for key,value in info.items():
#     print(key+ " : "+ str(value))

'''
sentence = "Python is great, and Python is fun!"
result : {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}
'''

sentence = "Python is great, and Python is fun!"

sentence = sentence.replace(',','')
sentence =sentence.replace('.','')
sentence =sentence.replace('!','')
sentence =sentence.replace('?','')
sentence.lower()

word_freq = {}
sentence_ = sentence.split(' ')
for word in sentence_:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(word_freq)