import re

# Getting email from user
email_address = input("Enter your personal email address '(you@(domain).com)': ")

# Regular expression pattern for validating an email address
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Function to validate email address
def validate_email(email):
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Validate the entered email address
if validate_email(email_address):
    print("The email address is valid.")
else:
    print("The email address is invalid.")