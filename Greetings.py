# Program to greet user and calculate  birth year
name = input("Enter your name:")
age = int((input("Enter your age: ")))

# calculate the year the user was born
birthday_year =int((input("Enter your birth year: ")))
current_year = 2025
age = current_year - birthday_year


# print a greeting with the user name and the calculated birth year
print(f"hello {name}, you are {age} year old") 

