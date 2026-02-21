## Day 1 - Working with Variables
## 20.02.2026

## print() method
# \n allow to retur\n on next line
print("Hello world!Hello World again")

# String Concatenation
print("Hello" + "Angela")
print("Hello" + " Angela")
print("Hello" + " " + "Angela")

# Input Function - Capture user input
input("What is your name? ")
print("Hello " + input("what is your name ?"))

# ---------------------------------------------------
# CHALLENGE
# fix the code below
print("Day 1 - string Manipulation")
print('string concatenation is done with the "+" sign.')
print('e.g. print("Hello" + "world")')
print("New Lines can be created with a backslash and n.")


# ---------------------------------------------------
# Write a program that print the number of a characthers in a users's name.
# Solution 1 - Saving in variables
# Ask the user for their name
name = input("Enter your name: ")

# Count the number of characters
lenght = len(name)

# print the lenght
print("The number of characters in your name is:", lenght)

# Solution 2 - Concatenating functions
print(len(input("Enter your name:")))

# ---------------------------------------------------------------------
# WRITE A PROGRAM THAT SWITCH THE VALUES STORED IN THE VARIABLE A AND B
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a = " + a)
print("b = " + b)
