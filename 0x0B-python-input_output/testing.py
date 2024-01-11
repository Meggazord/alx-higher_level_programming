import json

# Serialization (Python object to JSON string)
data_to_serialize = {'name': 'John', 'age': 30, 'city': 'New York'}
serialized_data = json.dumps(data_to_serialize)

print(data_to_serialize)

print(serialized_data)

# Deserialization (JSON string to Python object)
deserialized_data = json.loads(serialized_data)

print(deserialized_data)
