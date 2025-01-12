# asking for username and age
name = input("Enter your name: \n")
age = int(input("Enter your age: \n")) 

user_details ={
    "name": name,
    "age": age
} 
# printing input ad dictionary
new_name = input("Enter the previous name to retrieve your information \n") 
if new_name in user_details.values():
    print(f"Name: {user_details['name']} \n Age: {user_details['age']}") 