# situation 1 
num = [1,2,3,4,5]
for i in range (len(num)):
    print (num[i])

# situation 2   it will do it stop at 20 as 0 is also counted 
for i in range (0,21):
    print (i)

# q1 shopping cart total 
prices = [12.99, 5.50, 23.00, 10.25, 4.99]
total = 0 
for i in range (0,5):
    total = total + prices[i] 
print (total)

# q2 search and filter 
numbers = [14, 7, 31, 88, 42, 19, 50, 3]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print (numbers[i])

# q3 grade classifier 
scores = [85, 42, 75, 90, 58, 33]
for i in range (len(scores)):
    if scores[i] >= 70:
        print ("pass")
    else:
        print ("fail")

# q4 the highest score finder 
scores = [72, 88, 95, 64, 91, 55]
highest_score = 0 
for i in range (len(scores)):
    if scores [i] > highest_score:
        highest_score = scores[i]
    print (highest_score)

# q5 Name length greeter 
names = ["Alice", "Bob", "Charlie", "Dianna","Ethan"]
for i in range(len(names)):
    print("Hello" + names[i], "your name has", len(names[i]), "letters")
