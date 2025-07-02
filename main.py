import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# String Handling
        #012345
# quote = "Python is fun"
# print(quote[0:7])

print("Sign Up Form")
user_name = input("Enter your username: ")
password = input("Enter the password: ")

password_main = password.strip()
user_name_main = user_name.strip()

print("Sign In Form")
user_name_main1 = input("Enter your username: ")
password_main1 = input("Enter you password: ")

if user_name_main1.strip() == user_name_main and password_main1 == password_main:
    print("login successful")
else:
    print("Invalid username/password")