# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "gender": "male"
}

# Accessing dictionary values
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person.get("city"))
print("Gender:", person.get("gender"))

# Modifying dictionary values
person["age"] = 31
person["city"] = "Los Angeles"

# Adding new key-value pairs to a dictionary
person["occupation"] = "Software Engineer"

# Removing key-value pairs from a dictionary
del person["gender"]
person.pop("city", None)  # Removes key "city", if exists, otherwise does nothing

# Checking if a key is in a dictionary
if "name" in person:
    print("Name is a key in the dictionary.")

# Checking the length of a dictionary
dict_len = len(person)
print("Length of dictionary:", dict_len)

# Getting all keys and values in a dictionary
keys = person.keys()
values = person.values()
items = person.items()
print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Copying a dictionary
person_copy = person.copy()

# Clearing all key-value pairs in a dictionary
person.clear()

# Creating a dictionary with default values
default_dict = {}
default_dict.setdefault("name", "Unknown")
default_dict.setdefault("age", 0)
print("Default Dictionary:", default_dict)

# Merging two dictionaries
dict1 = {"name": "John", "age": 30}
dict2 = {"city": "New York", "gender": "male"}
merged_dict = dict1.copy()
merged_dict.update(dict2)
print("Merged Dictionary:", merged_dict)
