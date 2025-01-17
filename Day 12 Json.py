import json

# Function to read JSON file and return data
def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found.")
        return None

# Function to get value based on user input
def get_value_from_json(data, key):
    return data.get(key, "Key not found.")

# Main script
filename = 'data.json'  # Replace with your JSON file name
data = read_json_file(filename)

if data:
    key = input("Enter the key to get the value: ")
    value = get_value_from_json(data, key)
    print(f"The value for '{key}' is: {value}")