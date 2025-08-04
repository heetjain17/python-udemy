import json

# A Python dictionary
python_data = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "credits": 4}
    ]
}

# Encode the Python dictionary into a JSON string
# "dumps" = DUMP to String
json_string = json.dumps(python_data)

print("--- Python Dictionary ---")
print(python_data)
print(type(python_data))

print("\n--- JSON String ---")
print(json_string)
print(type(json_string))