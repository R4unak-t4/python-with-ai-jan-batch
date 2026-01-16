# control flow

# For & while

# range(5) --> range(0,5) --> [0,1,2,3,4]
# range(0,5)
#       a,b
'''
i --> 0
i --> 1
i --> 2
i --> 3
i --> 4
'''

# for i in range(0,6):
#     if i == 0:
#         print("0 is neither odd nor even")
#     elif i%2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')

# while
# num = 0
# while num <= 20:
#
#     if num == 10:
#         break
#
#
#     if num % 2 != 0:
#         num +=1
#         continue
#
#     print(num)
#     num += 1

# % --> remainder

# List

# list is enclosed in square brackets : []

arr = [20,"raunak",True,15.6]

name = "raunak"
age = 20
height = 173.5
weight = 64.56
isMale = True

info = ["raunak",20,173.5,64.56,True]
#        0       1   2      3     4

print(info[3])
# replacing value in a list
info[0] = 'Thapa'
print(info[0])

# .pop()
last = info.pop()
print(last)
print(info)

# .append()
info.append("hello")
print(info)

# .insert(idx,ele)
info.insert(2,'world')
print(info)

# [1,2,3,4,5]
# lst = [1,2,3,4,5]
# for i in range(2):
#     last = lst.pop()
#     lst.insert(0,last)
# print(lst)