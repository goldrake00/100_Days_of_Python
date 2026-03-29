# DATA TYPES

# String
# stampa la e di hello
print("hello"[1])

# Integer
print(123 + 456)
print(123_456_789)

# Float
3.14

# Boolean
True
False

# Le funzioni vengono eseguite dall'interno verso l'esterno
# 1. str trasforma integer in una stringa
# 2. len calcola la lunghezza della string
# 3. Print stampa la lunghezza della stringa
print(len(str(123)))


# type() serve a identificate il tipo di dato
pippo = len(str(123))
print(type(pippo))


# Type conversion (int->str)
# Si puo concatenare solo stringhe. Non si puo mischiare stringhe con integer.
# Per questo motivo si puo usare str() se si vuole trasformare un integer in una stringa

num_char = len(input("What's your name?"))
new_num_chart = str(num_char)
print("Your namen has " + new_num_chart + " characters.")

# ++++++++++++++++++++EXERCISE+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Write a program that adds the digits in a 2 digits number.
#  e.g. if the input was 35, then the output should be 3+5=8

# Capture the user input
two_digit_number = input("type a two digit number: ")

# Get the first and second digits using subscritpting then convert string to int.
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])

# Add the two digits together
sum = first_number + second_number
print(sum)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# MATHEMATICAL OPERATIONS
# PEMDAS stand for prio of calculation execution
# ()    Parhentesis
# **    Exponential
# * /   Moltiplication and division same prio.LEFT to RIGT give prio
# + -   Same as above


# ++++++++++++++++++++EXERCISE+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##  BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# User Input are always string.
# Convert strings into float and integer
h = float(height)
w = int(weight)

bmi = w / h**2
print(bmi)

# You can only concatenate strings and BMI is a FLOAT
# Therefore convert FLOAT to STRING
string_bmi = str(bmi)
print("Your BMI is = " + string_bmi)

# Cut BMI value after the coma
bmi_as_int = int(bmi)
print(bmi_as_int)

# Convert the INT into STRING ready for string concatenation
bmi_as_string = str(bmi_as_int)
print("Your BMI is = " + bmi_as_string)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# NUMBER MANIPULATION AND F-STRING

# Round decimal number
print(round(8 / 3))

# Round decimal number,specifying how many number after the coma
print(round(8 / 3, 2))

# Cutting Off numbers after coma (not rounding)
# Using 2 // return an integer and with 1 / return a float
print(8 // 3)


# Incrementals - Manipulate a value based on his previous value
score = 0
score = score + 1
# score = score + 1 means take the prevoius score and add 1
# this can be written as score += 1
print("score is = " + str(score))

# F-String - sove the problem by printing different type of values
# By print() only string can be concatenated

# example: Given an integer, a float and a boolean - concatenatete into a string

score = 0
height = 1.8
isWinning = True

# 1 Method - Converting types into strings
print(
    "Your score is" + str(score),
    "Your height is" + str(height),
    "boolean value is " + str(isWinning),
)

# 2 Method - Using F-String
print(f"Your score is {score},your height is{height},boolean value is{isWinning}")


# ++++++++++++++++++++EXERCISE+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Assuming you live til 90 years
# Ask user: What is your current age ?
# You have x days, y weeks , and z month left

## Interactive Exercise - 3 | Left Time to 90 :)
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
year_left = 90 - int(age)
day_left = year_left * 365
month_left = round(day_left / 30)
week_left = year_left * 52

print(f"You have {day_left} days, {week_left} weeks, and, {month_left} months left")
