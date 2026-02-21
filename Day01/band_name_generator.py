# 1. Create a greeting for the program
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and the pet and show their band name.
# 5. Make sure the input cursor shows on a new line
 
print("Welcome to the Band name Generator")
city = input("What's of city you grew up in?\n")
pet_name = input("What's yout pet's name?\n")
band_name = city + " " + pet_name
print("Your band name could be " + band_name)
