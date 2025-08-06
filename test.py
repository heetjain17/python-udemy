import json

filename = "data.json"

try:
    # Read the data directly from the file
    # "load" = LOAD from File
    with open(filename, 'r', encoding='utf-8') as file:
        python_data = json.load(file)

    print("Data loaded from file:")
    print(python_data)
    print(f"Name from file: {python_data['name']}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")