# 1. Write a program that prints the integers from 1 to 100. But for multiples of 
# three print "Fizz" instead of the number, and for multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

#print(list(range(1,101)))
#print(num)
#num = [1,2,15,30,3]

num = (range(1,101))
for  i in num:
 if (i % 5 == 0 and i % 3 == 0):
        print("FizzBuzz")
 elif i % 3 == 0:
        print("Fizz")
 elif  i % 5 == 0:
        print("Buzz")
 else:
    print(i)


# 2. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

oldlist = [1,1,1,1,2,2,3,3,3,3,4,5, 6,7,8,8,9,9,10,11,12,13,13,14,14,15,16]
newlist = set(oldlist)
print(newlist)

#3 create a program that stores value. Users are expected to guess the number. 
# if the user guesses correctly, return "You win", else, return "Try again"

r = 5
while True:
    option = input("""Input your lucky number: """)
    if int(option) == r:
        print("You win")
        break
    elif int(option) != r:
         print("Try again")
    choice = input("Do you want to try again now? Y/N")
    if choice.lower() == "y":
        continue
    else:
        print("Better luck next time")
        break
    
     
# 4. create a program that finds the largest of 3 numbers entered by the user

def largest_num():

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3

    # Print the largest number
    print(largest)

# Call the function to find the largest number
largest_num()

# 5. create a program that takes a score and shows the grade based on the score
# eg.
# 90 - 100 ("Grade A")
# 70 - 89 ("Grade B")
# 50 - 69 ("Grade c")
# 30 - 49 ("Grade D")
# 0 - 29 ("Grade F")

def calculate_grade(score):
    if 90 <= score <= 100:
         print("Grade A")
    elif 70 <= score <= 89:
        print("Grade B")
    elif 50 <= score <= 69:
        print("Grade C")
    elif 30 <= score <= 49:
        print("Grade D")
    elif 0 <= score <= 29:
          print("Grade F")
    else:
        print("invalid score")

score = int(input("Enter the score: "))
result = calculate_grade(score)

# 6. words = "I am here"
# print out the word in reverse to read "here am I"
words = "I am here"
words2 = words.split()
print(" ".join(reversed(words2)))

#7 . Create a program with a function that takes a number and prints 
#the number of digits in the number. It should work for numbers with decimals, too.

def count_length(howlong):
     print(len(howlong))

howlong = str(input("enter your number:  "))
countresult = count_length(howlong)

# 8. Create a program, longest.py, that has a function that takes one 
# string argument and prints a sentence indicating the longest word in that string. 
# If there is more than one word print only the first. Your print statement should read:
# “The longest word is x”
# Where x = the longest word. The word should be all lowercase

def longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    print("The longest word is", longest_word.lower())

sentence = str(input("Please enter your sentence "))
longest_word(sentence)

#  9. Create a program, that has a function that takes one string argument and prints a sentence indicating if the text is a palindrome. The function should consider only the alphanumeric characters in the string, and not depend on capitalization, punctuation, or whitespace.
# If your string is a palindrome it should print:
# It is a palindrome!
# If it is not a palindrome, it should print:
# It is not a palindrome!(

def palindrome(testwords):
     text = ''.join(char.lower() for char in testwords if char.isalnum())
     if text == text[::-1]:
        print("It is a palindrome!")
     else:
        print("It is not a palindrome!")

testwords= str(input("Please input your words:  "))

palindrome(testwords)

#10 2Write a program to print times tables. If you enter a number,
# it should generate the table for that number.
# Eg. If user enter 2,
# it should generate
# 2x1 = 2
# 2x2 = 4
# …
# Up to 2 x 12 = 24

def generate_times_table(number):
    i = 1
    while i <= 12:
        result = number * i
        print(f"{number} x {i} = {result}")
        i += 1

number = int(input("Enter a number to generate times table: "))
generate_times_table(number)