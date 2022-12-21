customer = {
    "name": "kedhar sairam",
    "age": "25",
    "is_verified": True
}

customer["name"] = "kedish"

customer["birthdate"] = "1997-Aug-28"

print(customer.get("name"))
print(customer.get("birthdate"))