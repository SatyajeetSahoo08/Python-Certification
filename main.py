import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# String Handling
        #012345
# quote = "Python is fun"
# print(quote[0:7])

# print("Sign Up Form")
# user_name = input("Enter your username: ")
# password = input("Enter the password: ")

# password_main = password.strip()
# user_name_main = user_name.strip()

# print("Sign In Form")
# user_name_main1 = input("Enter your username: ")
# password_main1 = input("Enter you password: ")

# if user_name_main1.strip() == user_name_main and password_main1 == password_main:
#     print("login successful")
# else:
#     print("Invalid username/password")
# print(2 ** 3 ** 2 ** 1)
# print('Peter\'s sister\'s name\'s \"Anna\"')
# i = 250
# while len(str(i)) > 72:
#     i *= 2
# else:
#     i //= 2
# print(i)

# n = 0
# while n < 4:
#     n += 1
#     print(n,end = " ")

# x = 0
# y = 2
# z = len("Python")
# x = y > z
# print(x)
# print(type(x))

# Val = 1
# Val2 = 0
# Val = Val ^ Val2
# Val2 = Val ^ Val2
# Val = Val ^ Val2

# print(val)

# z, y, x = 2, 1, 0
# x, z = z, y
# y = y - z
# x= 2, y = 0, z = 1
# # put line here
# x, y, z = y, z, x
# B. z, y, x = x, z, y
# C. y, z, x = x, y, z
# print(x, y, z)
# output = 0,1,2

# a = 0
# b = a ** 0
# if b < a + 1:
#     c = 1
# elif b == 1:
#     c = 2
# else:
#     c = 3
# print(a + b + c)

# i = 10
# while i > 0 :
#     i -= 3
#     print("*")
#     if i <= 3:
#         break
# else:
#     print("*")

# Example 1
# for i in range(1, 4, 2):
#     print("*")

# # Example 2
# for i in range(1, 4, 2):
#     print("*", end="")

# # Example 3
# for i in range(1, 4, 2):
#     print("*", end="**")

# Example 4
# for i in range(1, 4, 2):
#     print("*", end="**")
# print("***")

# x = "20"
# y = "30"
# print(x > y)

# s = "Hello, Python!"
# print(s[-14:15])

# lst = ["A", "B", "C", 2, 4]
# del lst[0:-2]
# print(lst)

# dict = { 'a': 1, 'b': 2, 'c': 3 }
# for item in dict:
#     print(item)

# s = 'python'
# for i in range(len(s)):
#     i = s[i].upper()
# print(s, end="")

# lst = [i // i for i in range(0,4)]
# sum = 0
# for n in lst:
#     sum += n
# print(sum)  

# lst = [[c for c in range(r)] for r in range(3)]
# for x in lst:
#     for y in x:
#         if y < 2:
#             print('*', end='')

# lst = [2 ** x for x in range(0, 11)]
# print(lst)
# print(lst[-1])

lst1 = "12,34"
lst2 = lst1.split(',')
print(len(lst1) < len(lst2))