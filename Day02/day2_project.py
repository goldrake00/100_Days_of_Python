## Day 2 - Understanding Data Types
## 15.03.2026
## ----------------------------
## DAY 2 PROJECT Tip Calculator
## ----------------------------

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Expected Result****
# Welcome to the tip calculator
# What was the total bill?$124.56
# What percentage tip would you like to give? 10,12,or 15? 12
# How many paople to split the bill? 7
# Each person should pay: $19.93

# Write your code below this line 👇

print("Welcome to the tip calculator !\n")
bill = round(float(input("What was the total bill?$ ")), 2)
tip_percent = int(input("What percentage tip would you like to give? 10,12,or 15? "))
n_people = int(input("How many paople to split the bill? "))
result = round((bill / n_people) * (1 + 1 / tip_percent), 2)
print(f"Each person should pay:{result}$")
