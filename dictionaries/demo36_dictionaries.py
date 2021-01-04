customer = {
    "name": "john Smith",
    "age": 30,
    # "age": 40,        # duplicates are not allowed in dictionaries
    "is_verified": True
}

print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate"))  # non existing elements will throw "none"
print(customer.get("birthdate", "January 01 1997"))  # adding a default value - "January 01 1997"

customer["name"] = "John Doe"
print(customer["name"])  # updating/changing a value
