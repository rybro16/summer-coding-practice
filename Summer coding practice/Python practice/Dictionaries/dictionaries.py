# A simple Python dictionary
person = {
    "name": "Alex",
    "age": 25,
    "city": "London"
}

# q1 character stats lookup accessing values
player = {
    "username": "DragonSlayer99",
    "level": 15,
    "health": 85.5,
    "is_alive": True
}
print(player["level"])
print(player["username"],"has", player["health"], "health left")

# q2 updating and adding new stats
player = {
    "username": "DragonSlayer99",
    "level": 15,
    "health": 85.5,
    "is_alive": True
}
player["health"] = player["health"] + 20
player["weapon"] = "Excalibur"
print(player)

# q3 safely checking and getting values 
inventory = {
    "potions": 3,
    "gold": 150,
    "keys": 1
}
print(inventory["potions"])
scrolls_count = inventory.get("scrolls", 0)
print(scrolls_count)

# q5 new dictionary 
cart = {

}
cart["python basics"] = 2
cart["data structures"] = 1
cart["python basics"] = 3
print(cart)

# q6 shopping cart total
cart = {
    "python basics": 3,
    "data structures": 1
}

prices = {
    "python basics": 15.00,
    "data structures": 25.00
}
totalbill = 0
for item in cart:
    totalbill = totalbill + (cart[item] * prices[item])

print(totalbill)