# used to store a key value pairs
customer = {
    "name":"John Smith",
    "age":30,
    "is_Verified": True
}
customer["name"] = "viCracker"
customer["birthdate"] = "June 6 1999"
print(customer.get("name"))
print(customer["birthdate"])