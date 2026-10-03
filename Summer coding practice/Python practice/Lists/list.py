list1 = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

def get_podium(list1):
    return list1[0:3]

list2 = get_podium(list1)
print(list2)

# q1 shopping cart manager 
cart = ["apples","bread", "butter"]
cart.append("milk")
cart.remove("bread")
cart[0] = "green apples"
print (cart)

# q2 high score leaderboard
scores = [120, 250, 310, 420, 500]
top_score = scores[-1]
print(top_score)
print(len(scores))
scores.append(550)
print(scores)

# q3 classroom seating 2d list
classroom = [
    ["Alice", "Bob", "Charlie"],   # Row 0
    ["David", "Eve", "Frank"]     # Row 1
]
print(classroom[0][2])
print(classroom[1][1])
classroom[1][1] = "Grace"
print(classroom)

# q4 inventory managment 
inventory = [
    ["Apples", "Bananas"],   # Shelf 0
    ["Milk", "Cheese"]      # Shelf 1
]
inventory[0].append("Oranges")
inventory.append(["Bread", "Butter"])
print(len(inventory))
print(inventory)

#q5 movies list
movies = [
    "Batman",
    "Superman",
    "Avengers: Doomsday",
    "Spider-Man: Brand New Day", 
    "The Odyssey", 
    "Jumanji",
]
first_three = movies[:3]
print(first_three)
middle_three = movies[2:5]
revlist = movies[::-1]
print(revlist)

# q6 fruits
market = [
    ["Apples", "Bananas", "Cherries"],   # Row 0: Row of basic fruit
    ["Dates", "Elderberries", "Figs"]    # Row 1: Row of exotic fruit
]
print(market[1][1])
market[0][1] = "Blueberries"
market[1].append("Grapes")
market[1].remove("Dates")
first_two_row0 = market[0][:2]
print(market)
