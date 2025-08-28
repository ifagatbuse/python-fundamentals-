# Project 8: Simple Dictionary
# Topic: Key-Value Pairs

person = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}

print("Name:", person["name"])
print("Age:", person["age"])

# add new key-value
person["job"] = "Engineer"
print("After adding job:", person)

# update value
person["age"] = 21
print("After updating age:", person)

# loop through dictionary
print("\nAll info:")
for key, value in person.items():
    print(key, ":", value)
