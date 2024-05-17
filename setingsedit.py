import json

# Sample JSON data
json_data = '{"name": "Alice", "age": 30, "city": "Los Angeles"}'

# Parse the JSON data
data = json.loads(json_data)

# Specify the field key to update
field_key = 'age'

# Update the specified field value
if field_key in data:
    data[field_key] += 1

# Convert the modified data back to JSON
modified_json = json.dumps(data)

print('Before Modifying:', json_data)
print('After Modifying:', modified_json)