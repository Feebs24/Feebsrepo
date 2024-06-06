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
record = "welcome to ARM"
first_name = 'Wale'
mail = """Dear Sir,
Here is my application for the role of DevOps Engineer
Thank you"""
words = "The is Wale's laptop"
phone_number = "123456789"
username = "    wale   "

# strings are immutable
print(record.capitalize())
print(record.upper())
print(first_name.lower())
print(len(record))
print(mail.count("e"))
print(mail.index("DevOps"))
print(mail[49:55])
print(words.endswith("p"))
print(words.startswith("t"))
print(username.strip())
print(record.split())

my_words = record.split()
print("-".join(my_words))

# List data type - for storing multiple values
# it is denoted by []

# mail[5]
staff = ["Linda", "Paul", "Mary", "John"]
print(type(mail))
print(type(staff))

# indexing a list
print(staff[3])

# slicing a list
print(" ".join(staff[1:3]))
print(staff[0:4:3])

# list methods
# print(len(staff))
staff.append("Wale")   # append add item to end of list
print(staff)

staff.pop(1)   # pop removes last item or indexed item
print(staff)

staff.remove("Wale")  # remove takes away the word supplied
print(staff)

words = "Wale goes to school"
words = words.split()
words.pop(0)
print(" ".join(words))

# words.clear() # removes all items in the list
# print(words)

sentence = words.copy()  # store duplicate of your data
print(sentence)

words.insert(0, "wale")   # specify the index to append the word
print(words)

words.reverse()  # return a reverse of the string
print(words)

words.sort() # arrange in ascending order
print(words)

words.extend(phone_number)   # merging 2 lists into one
print(words)

print(words[4:])

print(phone_number)
phone_number = phone_number.replace("7","6")
print(phone_number)

print(phone_number.replace(phone_number[1],"3"))

# nested list - a list inside another list
matrix = [[1,2,3],[4,5,6],[1,2,3]]
print(matrix[1][1])
print(matrix[2][2])


# dictionary - are unordered key-value pair
# denoted by {}

staff = ["wale","mary","john"]
staff = {"name":"wale", "age":20,"gender":"male"}
print(staff["age"])
print(staff["gender"])

staff = [{"name":"wale", "age":20,"gender":"male"},
        {"name":"mary", "age":30,"gender":"female"},
        {"name":"john", "age":25,"gender":"male"}]



print(staff[1]["gender"])

address = {"street":"70c Allen Avenue", "city":{"province":"Ikeja", "postcode":[10111, 23401]}}
print(address["city"]["postcode"][1])

staff = {"name":"wale", "age":20,"gender":"male"}
print(staff)

# dictionary methods
# staff.update({"email":"johndoe@gmail.com"})
# print(staff)

# staff.update({"email":"wale@gmail.com"})
# print(staff)

# staff = [{"name":"wale", "age":20,"gender":"male"},
#         {"name":"mary", "age":30,"gender":"female"},
#         {"name":"john", "age":25,"gender":"male"}]

# staff[1].update({"email":"mary@gmail.com"})
# print(staff)

staff = {"name":"wale", "age":20,"gender":"male"}

print(staff.get("name"))    # return the value of the key supplied

print(staff.values())   # returns all the values

print(staff.keys())  # returns all the keys

print(staff.items())   # returns both the keys and values

staff.popitem()     # remove the last key-value pair
print(staff)    

staff.pop("age")    # remove the key-value pair of the key supplied
print(staff)  


staff.setdefault("phone")  # if no value is supplied, None is used as default
print(staff)

keys = ["Mary","John", "Mike"]
print(dict.fromkeys(keys,"7 days"))

print(dict.fromkeys(keys,{"work_days":"7 days"}))

# assigning different values for different pair

staff = ["Linda","Mary","Paul"]
gender = ["Female", "Female", "Male"]
print(list(zip(staff, gender)))

# Tuple data type - is for storing immutable values
# it is denoted by ()

days_of_the_week = ("Mon","Tue","Wed")
print(days_of_the_week[2])

result = tuple([20, 50, 10])
print(type(result))

# conversion of data type to another data type
int("5")
str(5)
list()
dict()

# sets - is used for storing unique values
# it is denoted by {}
num1 = {1,2,3}
num2 = {3,4,5}
print(type(num1))

# intersection - what is common to both set
print(num1.intersection(num2))

# union - combination of all in num1 and num2
print(num1.union(num2))

# difference - what is in num1 that is not in num2
print(num1.difference(num2))

# symmetric difference - what is in num1 and not in num2 and what is in num2 and not in num1 
print(num1.symmetric_difference(num2))

data = {1,1,1,1,1,1,11,2,2,2,2,2,2,2,2,11,1,1,1,1,1}
print(data)

points = [1,1,1,1,1,1,11,2,2,2,2,2,2,2,2,11,1,1,1,1,1]
print(set(points))


num1.symmetric_difference_update(num2)
print(num1)

# Boolean - for storing True or False
# 0 is False while 1 is true
is_admin  = bool("True")

print(6 > 5)

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

account_balance = 123.47264783524216547
print(int(account_balance))
print(str(account_balance))
print(str("%.2f" %account_balance))

y = None
print(y)


