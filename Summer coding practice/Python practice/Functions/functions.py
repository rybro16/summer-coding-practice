# q1 shop list
items = ["Apples", "Milk", "Bread"]
def shopping_list(items):
    for i in range (len(items)):
        print(items[i])

shopping_list(items)

# q2 prices
items = ["Shirt", "Pants", "Hat"]
prices = [25, 40, 15]
def pair_prices(items, prices):
    for i in range(len(items)):
        print(f"{items[i]} costs {prices[i]}")

pair_prices(items, prices)

# q3 Modifying a List & Returning
prices = [10, 20, 100]
def add_tax(prices):
    for i in range(len(prices)):
        prices[i] = prices[i] * 1.10
    return prices

print(add_tax(prices))

# q4 Filtering Data
names = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [12, 0, 5, 0]
def get_out_of_stock(names,stocks):
    out_of_stock = []
    for i in range(len(stocks)):
        if stocks[i] == 0:
            out_of_stock.append(names[i])
    return out_of_stock            

# q5 Threshold Filtering
scores = [45, 82, 67, 39, 90, 55]
def get_passing_scores(scores):
    Pass = []
    for i in range(len(scores)):
        if scores[i] >= 50:
            Pass.append(scores[i])
    return Pass
print(get_passing_scores(scores))

# q6 Dual-List Filtering
employees = ["Alice", "Bob", "Charlie", "David"]
years = [2, 7, 1, 5]
def get_veterans(employees, years):
    experience = []
    for i in range(len(years)):
        if years[i]>=5:
            experience.append(employees[i])
    return experience
print(get_veterans(employees, years))

# q7 Accumulator Pattern (Totaling)
prices = [12.50, 3.99, 25.00, 8.50]
def calculate_total(prices):
    total = 0
    for i in range(len(prices)):
        total = total + prices[i]
    return total

print(calculate_total(prices))

# q8 Conditional Modification
prices = [15, 60, 100, 30]

def apply_discount(prices):
    for i in range(len(prices)):
        if prices[i]>= 50:
            prices[i] = prices[i]*0.8
    return prices
print(apply_discount(prices))

# q9 Multi-Condition Dual-List Filtering
names = ["Laptops", "Mice", "Keyboards", "Monitors", "Headsets"]
stock = [12, 2, 0, 4, 15]

def get_reorder_items(names, stock):
    new_list = []
    for i in range(len(stock)):
        if stock[i]<5 and stock[i]>0:
            new_list.append(names[i])
    return new_list
            

print(get_reorder_items(names, stock))

# q10 Searching Parallel Lists for a Maximum
names = ["Alice", "Bob", "Charlie", "David"]
scores = [88, 95, 72, 91]

def get_top_student(names, scores):
    highest_score = scores[0]
    top_student = names[0]
    for i in range(len(scores)):
        if scores[i]>highest_score:
            highest_score = scores[i]
            top_student = names[i]

    return(f"{top_student} has a score of {highest_score}")

print(get_top_student(names, scores)) 

# q11 Target Search and Update
names = ["Apples", "Bananas", "Oranges"]
stock = [10, 5, 8]

def restock_item(names, stock, target_item, amount):
    for i in range (len(stock)):
        if target_item == names[i]:
            stock[i] = stock[i] + amount 
    return stock
print(restock_item(names, stock, "Bananas", 15))

# q12 Search with Early Exit (Boolean Check)
names = ["Laptop", "Mouse", "Keyboard"]
stock = [0, 5, 2]
def is_in_stock(names, stock, target_item):
    for i in range(len(stock)):
        if target_item == names[i] and stock[i]>0:
            return True
        
    return False
print(is_in_stock(names, stock, "Mouse"))

# q13 Computing Averages Across Parallel Lists
names = ["Alice", "Bob", "Charlie", "David"]
salaries = [50000, 70000, 60000, 100000]

def get_above_average_salaries(names, salaries):
    morethanaverage = []
    total = 0
    for i in range (len(salaries)):
        total = total + salaries[i]
    average = total / len(salaries)
    for i in range (len(salaries)):
        if salaries[i]>average:
            morethanaverage.append(names[i])
    return morethanaverage

print(get_above_average_salaries(names, salaries))