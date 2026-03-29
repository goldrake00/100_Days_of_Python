## Day 3 - Conditional Operators
## 16.03.2023

## CONDITIONAL OPERATORS ######

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
else:
    print("Sorry, you have to grow taller before yo can ride.")

# ######### CHALLENGE: Idenfiy if a given number is odd or Even ############

# Odd or Even Exercise
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# # NESTED IF/ELSE ###### With only one condition

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Your ticket costs 12$")
    else:
        print("Your ticket costs 7$")
else:
    print("Sorry, you have to grow taller before yo can ride.")

# # NESTED IF/ELSE ###### With only MULTIPLE conditions


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket costs 5$")
    elif age < 18:
        print("Your ticket costs 7$")
    else:
        print("Your ticket costs 12$")
else:
    print("Sorry, you have to grow taller before yo can ride.")


# ######### CHALLENGE:BMI Calculator and interpretation ############
## BMI 2.0 Exercise
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / (height**2), 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight ")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you are normal ")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are overweight ")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese ")
else:
    print(f"Your BMI is {bmi} and you are clinically obese ")


## Determine Leap Year Exercise
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is a NOT a leap year")
    else:
        print("This is a leap year")
else:
    print("This is a NOT a leap year")


# # NESTED IF/ELSE ###### With  MULTIPLE conditions
# Add 3$ in case customer wants a picture

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        price = 5
        photo_price = 3
        photo = input("Do you want a picture? Y/N ")
        if photo == "Y":
            total_cost = price + photo_price
            print(f"Your total cost is {total_cost}$")
        if photo == "N":
            print(f"Your ticket costs {price}$")
    elif age < 18:
        price = 7
        photo_price = 3
        photo = input("Do you want a picture? Y/N ")
        if photo == "Y":
            total_cost = price + photo_price
            print(f"Your total cost is {total_cost}$")
        if photo == "N":
            print(f"Your ticket costs {price}$")
    else:
        price = 12
        photo_price = 3
        photo = input("Do you want a picture? Y/N ")
        if photo == "Y":
            total_cost = price + photo_price
            print(f"Your total cost is {total_cost}$")
        if photo == "N":
            print(f"Your ticket costs {price}$")

else:
    print("Sorry, you have to grow taller before yo can ride.")


# ######### CHALLENGE:PIZZA ORDER ############
## Pizza Delivery Challenge
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Price List
small_pizza = 15
medium_pizza = 20
large_pizza = 25

peperoni_small = 2
peperoni_medium_large = 3

price_extra_cheese = 1


if size == "S":
    if add_pepperoni == "N" and extra_cheese == "N":
        bill = small_pizza
        print(f"Your final bill is {bill}")
    if add_pepperoni == "N" and extra_cheese == "Y":
        bill = small_pizza + price_extra_cheese
        print(f"Your final bill is {bill}")
    if add_pepperoni == "Y" and extra_cheese == "N":
        bill = small_pizza + peperoni_small
        print(f"Your final bill is {bill}")
    if add_pepperoni == "Y" and extra_cheese == "Y":
        bill = small_pizza + peperoni_small + price_extra_cheese
        print(f"Your final bill is {bill}")


if size == "M":
    if add_pepperoni == "N" and extra_cheese == "N":
        bill = medium_pizza
        print(f"Your final bill is {bill}")
    if add_pepperoni == "N" and extra_cheese == "Y":
        bill = medium_pizza + price_extra_cheese
        print(f"Your final bill is {bill}")
    if add_pepperoni == "Y" and extra_cheese == "N":
        bill = medium_pizza + peperoni_medium_large
        print(f"Your final bill is {bill}")
    if add_pepperoni == "Y" and extra_cheese == "Y":
        bill = medium_pizza + peperoni_medium_large + price_extra_cheese
        print(f"Your final bill is {bill}")


if size == "L":
    if add_pepperoni == "N" and extra_cheese == "N":
        bill = large_pizza
        print(f"Your final bill is {bill}")
    if add_pepperoni == "N" and extra_cheese == "Y":
        bill = large_pizza + price_extra_cheese
        print(f"Your final bill is {bill}")
    if add_pepperoni == "Y" and extra_cheese == "N":
        bill = large_pizza + peperoni_medium_large
        print(f"Your final bill is {bill}")
    if add_pepperoni == "Y" and extra_cheese == "Y":
        bill = large_pizza + peperoni_medium_large + price_extra_cheese
        print(f"Your final bill is {bill}")


##Love Calculator Exercise
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# Remeber.You can concatenate only strings, not INT
string_name = name1.lower() + name2.lower()

total_tens = (
    string_name.count("t")
    + string_name.count("r")
    + string_name.count("u")
    + string_name.count("e")
)
total_unists = (
    string_name.count("l")
    + string_name.count("o")
    + string_name.count("v")
    + string_name.count("e")
)

score_love = int(str(total_tens) + str(total_unists))

if score_love < 10 or score_love > 90:
    print(f"Your love score is {score_love}, you go together like coke and mentos")

elif 40 < score_love < 50:
    print(f"Your love score is {score_love}, you are alright together")

else:
    print(f"Your love score is {score_love}")
