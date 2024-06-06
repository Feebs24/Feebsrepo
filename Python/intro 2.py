# introduction
# installation
# input and output
# variables
# data types
# strings, list, dictionary, tuple, sets, numbers, None
# operators
# control flow
# loops
# functions
# higher order function 
# module 
# packages
# working with file
# Exercises

# How to display output
# print(2+2)
# print("Welcome to DevOps")
# print("2+2=",2 + 2)

# the # symbols is for commenting your code

# Accepting input from user
# input("Enter your name: ")

# Variables - are used for storing data
# x = 5
# print(x)

# rules of naming variables
#1. it should be descriptive
# tp = 50000
# total_price = 50000
# print(total_price)

#2. case sensitive
# firstName = "wale"
# Firstname = "John"
# print(FirstName)

#snake casing
# first_name
# # thisisthefinalresult
# this_is_the_final_result

#3. variable cannot contain spaces
# first name = "wale"

# 4. variable cannot be a reserved word
# print_values = "Welcome to ARM"
# print(print_values)

# 5. Variable cannot start with a number
# numbers2 = 2 + 2

# 6. variable cannot contain symbols except an underscore
# _result = 40000

# name = 5
# name = "Mary"
# print(name)

# Data Types - defined how data are stored and manipulated
# number = 5
# print(number + 5)
# name = "wale"
# print(name + 5)

# strings - is for storing sequence of characters
# it is denoted by single quote, double quote or triple quote
record = "Welcome to ARM"
first_name = 'Wale'
mail = """Dear Sir,
Here is my application for the role of DevOps Engineer
Thank you"""
words = "The is Wale's laptop"

# indexing - is how the data are orderly stored
# print(record[4])
# print(mail[5])
# print(record[12])
# print(record[-2])

# # slicing - is for extracting multiple characters
# print(record[-3:])
# print(record[:6])
# print(mail[5:8])

# taking steps
phone_number = "123456789"
# print(phone_number[1::2])

# print out 8765432
# print(phone_number[-2:-8])

# print(phone_number[-2::-1])
# print(phone_number[6::-1])
print(phone_number[-2:-9:-1])
print(phone_number[7:0:-1])

# string methods
# record = "welcome to ARM"
# first_name = 'Wale'
# mail = """Dear Sir,
# Here is my application for the role of DevOps Engineer
# Thank you"""
# words = "The is Wale's laptop"
# phone_number = "123456789"
# username = "    wale   "

# # strings are immutable
# print(record.capitalize())
# print(record.upper())
# print(first_name.lower())
# print(len(record))
# print(mail.count("e"))
# print(mail.index("DevOps"))
# print(mail[49:55])
# print(words.endswith("p"))
# print(words.startswith("t"))
# print(username.strip())
# print(record.split())

# my_words = record.split()
# print("-".join(my_words))

# # List data type - for storing multiple values
# # it is denoted by []

# # mail[5]
# staff = ["Linda", "Paul", "Mary", "John"]
# print(type(mail))
# print(type(staff))

# # indexing a list
# print(staff[3])

# # slicing a list
# print(" ".join(staff[1:3]))
# print(staff[0:4:3])

# # list methods
# # print(len(staff))
# staff.append("Wale")   # append add item to end of list
# print(staff)

# staff.pop(1)   # pop removes last item or indexed item
# print(staff)

# staff.remove("Wale")  # remove takes away the word supplied
# print(staff)

# words = "Wale goes to school"
# words = words.split()
# words.pop(0)
# print(" ".join(words))

# # words.clear() # removes all items in the list
# # print(words)

# sentence = words.copy()  # store duplicate of your data
# print(sentence)

# words.insert(0, "wale")   # specify the index to append the word
# print(words)

# words.reverse()  # return a reverse of the string
# print(words)

# words.sort() # arrange in ascending order
# print(words)

# words.extend(phone_number)   # merging 2 lists into one
# print(words)

# print(words[4:])

# print(phone_number)
# phone_number = phone_number.replace("7","6")
# print(phone_number)

# print(phone_number.replace(phone_number[1],"3"))

# # nested list - a list inside another list
# matrix = [[1,2,3],[4,5,6],[1,2,3]]
# print(matrix[1][1])
# print(matrix[2][2])


# # dictionary - are unordered key-value pair
# # denoted by {}

# staff = ["wale","mary","john"]
# staff = {"name":"wale", "age":20,"gender":"male"}
# print(staff["age"])
# print(staff["gender"])

# staff = [{"name":"wale", "age":20,"gender":"male"},
#         {"name":"mary", "age":30,"gender":"female"},
#         {"name":"john", "age":25,"gender":"male"}]



# print(staff[1]["gender"])

# address = {"street":"70c Allen Avenue", "city":{"province":"Ikeja", "postcode":[10111, 23401]}}
# print(address["city"]["postcode"][1])

# staff = {"name":"wale", "age":20,"gender":"male"}
# print(staff)

# # dictionary methods
# # staff.update({"email":"johndoe@gmail.com"})
# # print(staff)

# # staff.update({"email":"wale@gmail.com"})
# # print(staff)

# # staff = [{"name":"wale", "age":20,"gender":"male"},
# #         {"name":"mary", "age":30,"gender":"female"},
# #         {"name":"john", "age":25,"gender":"male"}]

# # staff[1].update({"email":"mary@gmail.com"})
# # print(staff)

# staff = {"name":"wale", "age":20,"gender":"male"}

# print(staff.get("name"))    # return the value of the key supplied

# print(staff.values())   # returns all the values

# print(staff.keys())  # returns all the keys

# print(staff.items())   # returns both the keys and values

# staff.popitem()     # remove the last key-value pair
# print(staff)    

# staff.pop("age")    # remove the key-value pair of the key supplied
# print(staff)  


# staff.setdefault("phone")  # if no value is supplied, None is used as default
# print(staff)

# keys = ["Mary","John", "Mike"]
# print(dict.fromkeys(keys,"7 days"))

# print(dict.fromkeys(keys,{"work_days":"7 days"}))

# # assigning different values for different pair

# staff = ["Linda","Mary","Paul"]
# gender = ["Female", "Female", "Male"]
# print(list(zip(staff, gender)))

# # Tuple data type - is for storing immutable values
# # it is denoted by ()

# days_of_the_week = ("Mon","Tue","Wed")
# print(days_of_the_week[2])

# result = tuple([20, 50, 10])
# print(type(result))

# # conversion of data type to another data type
# int("5")
# str(5)
# list()
# dict()

# # sets - is used for storing unique values
# # it is denoted by {}
# num1 = {1,2,3}
# num2 = {3,4,5}
# print(type(num1))

# # intersection - what is common to both set
# print(num1.intersection(num2))

# # union - combination of all in num1 and num2
# print(num1.union(num2))

# # difference - what is in num1 that is not in num2
# print(num1.difference(num2))

# # symmetric difference - what is in num1 and not in num2 and what is in num2 and not in num1 
# print(num1.symmetric_difference(num2))

# data = {1,1,1,1,1,1,11,2,2,2,2,2,2,2,2,11,1,1,1,1,1}
# print(data)

# points = [1,1,1,1,1,1,11,2,2,2,2,2,2,2,2,11,1,1,1,1,1]
# print(set(points))


# num1.symmetric_difference_update(num2)
# print(num1)

# # Boolean - for storing True or False
# # 0 is False while 1 is true
# is_admin  = bool("True")

# print(6 > 5)

# if is_admin == 1:
#     print("Welcome admin")
# else:
#     print("Not authorized")

# numeric data type - it is for storing integers, float, complex numbers

# salary = int(100000.56)
# age = float(18)

# print(type(salary))
# print(type(age))
# print(salary)
# print(age)

# formatting numerical values

# account_balance = 123.47264783524216547
# print(int(account_balance))
# print(str(account_balance))
# print(str("%.2f" %account_balance))

# y = None
# print(y)

# operators
# arithmetic operators   +, -, /, *, //, %, **
# x = 5
# y = 2
# print(x + y)
# print(x - y)
# print(x * y)
# print(x ** y)  #exponent - raised to the power of
# print(x / y)
# print( x // y)   #floor division return the value without the decimals/remainder
# print(x % y)    #modulus return the remainder

# # comparison operator  >,  <, >= , <=, ==, !=
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)
# print(x == y)
# print( x != y)

# # logical operator  and, or, not
# print(5 > 4 and 2 > 3)  #and means both condition must be true
# print(3 > 6 or 4 > 2) #or means one condition must be met
# print(not(3 > 2))  # not returns the opposite of the expected value

# # assignment operator  +=, -=, /=, *=, //=. %=
# x = 5
# y = 3
# x += y    #  x = x + y
# print(x)

# x -= y    # x = x - y
# print(x)

# # membership operator - used to check if an element is a member of a list
# numbers = [1,2,3,4,5]
# print(3 in numbers)

# control flow
# age = 17
# if age >= 18:
#     print("You can vote")
# else:
#     print("Not eligible")

# number = -5
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# elif number == 0:
#     print("Zero")
# else:
#     print("Unknown number")

# write a code that checks if someone is 18 and above and a Nigerian before then can vote

# age = int(input("Enter your age: "))
# country = input("Enter your country name: ")
# if age >= 18 and country.capitalize() == "Nigeria":
#     print("You can vote")
# else:
#     print("Not eligible")

# Loops - it is used to repeat a task until certain condition is met
# while loop - indefinite loop 

# while loop (initial value, condition, action, increment)
# num = 1            #initial value
# while num <= 5:   # condition
#     print(num)    # action
#     num += 1   # increment


# while True:
#     option = input("""Press B to check balance
#                 Press D to deposit
#                 Press W to withdraw: """)
#     if option.lower() == "b":
#         print("Your balance is xyz")
#     elif option.lower() == "d":
#         print("deposit successful")
#     elif option.lower() == "w":
#         print("withdrawal successful")

#     choice = input("Do you want to perform another transaction? Y/N")
#     if choice.lower() == "y":
#         continue
#     else:
#         print("Have a nice day")
#         break


# 2
# 4
# 6
# 8
# 10

# x = 2
# while x <= 10:
#     print(x)
#     x += 2

# data = [1,2,3,4,5,6,7,8,9,10]
# for i in data:
#     if i % 2 == 0:
#         print(i)

# x = 2
# while x <= 10:
#     if x % 2 == 0:
#         print(x)
#         x += 2

# num=2
# while num<=10:
#     if num%2==0:
#         print(num)
#     num+=1


# for loop - definite
# data = [1,2,3,4,5,6,7,8,9,10]
# for i in data:
#     if i % 2 == 0:
#         print(i)

# print(list(range(3,11,10-5)))

# for i in range(11):
#     print(i)
# print out all the words that start with T
words = "ARM DevOps Training with python. Thank you. Tom"
# words = words.split()
# for item in words:
#     if item.startswith("T"):
#         print(item)

# words = "ARM DevOps Training with python. Thank you. Tom"
# words_list=words.split(" ")
# print(words_list)
# for i in words_list:
#     if i.lower().startswith("t"):
#          print(i)

# for i in words.split():
#     if i[0].lower() == 't':
#         print(i)

# functions - is a block of code that is reusable
# def add_it():
#     return int(2 + 2)

# print(add_it())

# function parameter
# num1 = input("Enter first number")
# num2 = input("Enter second number")
# def add_it(x,y):
#     return x + y

# print(add_it(num1, num2))

#lambda - anonymous function
# lambda x,y: x + y

# higher order function - passing function as a parameter map, filter, reduce
data = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for item in data:
#     sum += item 
# print(sum)

# map - same number of items that comes in goes out
# filter - only items that meet the condition
# reduce - returns a single value

print(list(map(lambda x:x*2,data)))
print(list(filter(lambda x:x % 2 == 0, data)))

from functools import reduce
print(reduce(lambda x,y:x + y, data))

# list comprehension
print([i * 2 for i in range(1,11) if i % 2 == 0])

staff = [{"name":"Joe", "age":30},
        {"name":"Mary", "age":20},
        {"name":"Paul", "age":40},
        {"name":"Linda", "age":35},
]

# sum the age of all staff who are above 30 years
# total_age = sum(person["age"] for person in staff)
# print(total_age)

# print(list(filter(lambda x: x["age"] > 30,staff)))
print(reduce(lambda x,y: x["age"] + y["age"], filter(lambda x: x["age"] > 30,staff)))

# args and kwargs
# def test(x,y,z):
#     return x + y 

# print(test(2,4,5))

# def sum_it(*args):
#     total = 0
#     for i in args:
#         total += i
# print(sum_it(5,10,15,50, 80, 70, 60, 500, 40))
# sample = {"name":"wale", "age":18}
# for i in sample.items():
#     print(i)


def staff(**kwargs):
    for k, v in kwargs.items():
        print("my name is", k, "I am", v, "years old")
        
print(staff(wale=18,Mary=20,Max=30,John=25))


# def demo(*args):
#     for i in args:
#         print(i)

# demo("wale",[1,2,3], "john", 50)


# match case

# color = "white"

# match color:
#     case "red" | "green" | "white":
#         print("red color")

#     case "blue" :
#         print("blue color")

#     case _:
#         print("unknown color")


# modules - separating your code into different component

# from calculator import *
# print(add_it(3,4))

# import calculator
# print(calculator.add_it(3,5))

# packages - combination of modules

# from PyDictionary import PyDictionary

# # d = PyDictionary()

# word = input("Enter the word to get the meaning: ")
# # print(d.meaning(word))

# print(PyDictionary().meaning(word))

# working with files
# creating files with python
# with open("wale.txt", "w") as file:
#     file.write("Welcome to DevOps Training")


# with open("wale.txt", "r") as file:
#     print(file.read())

# file = open("wale.txt", "a")
# file.write("Python is easy")
# file.close()


# os module
import os
# os.remove("wale.txt")
# os.mkdir("ARM")
# print(os.getcwd())
# print(os.listdir())
# os.chdir("ARM")
# os.chdir("devops")
# os.mkdir("devops")
# file = open("wale.txt", "w")
# file.write("Python is easy")
# file.close()
# try and catch

# file = open("demo/wale.txt", "w")
# file.write("Python is easy")
# file.close()

# print(os.path)
# if os.path.exists("demo\arm.txt"):
#     print("File already exist")
# else:
#     file = open("demo/arm.txt", "w")
#     file.write("Python is easy")
#     file.close()


# handling exceptions

x = 5
y = 0

try:
    result = x/y
except ZeroDivisionError:
    print("You cannot divide by zero")
except EOFError:
    print("End of file error")
finally:
    print("The end")