# Understanding Dictionaries
# Create a dictionary named car with the following keys: make, model, year, and color. Assign appropriate values to each key.

#     "make": "Toyota",

#     "model": "Camry",

#     "year": 2020,

#     "color": "Blue"

# Print the value associated with the model key.

# Add a new key called owner and assign it the name "Rahul".

# Print the entire dictionary.

# Expected Result:



# Car model: Camry
# Updated car dictionary: {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue', 'owner': 'Rahul'}

car = {
    "make": "Toyota",

    "model": "Camry",

    "year": 2020,

    "color": "Blue"
}

print("Car model:", car["model"])

# car["owner"] = "Rahul" # adding new key value using assignment operator

# car.update({"owner":"Rahul"}) # using update method here you can multiple key value at once.

car = car | {"owner":"Rahul"} # another way is to merge using operator |



print("Updated car dictionary:",car)
