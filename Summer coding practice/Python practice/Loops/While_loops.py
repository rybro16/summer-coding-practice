# situation 1 
i = 0 
while i < 5:
    print (i)
    i = i + 1     # without this line it will be an infinite loop 

# example shopping cart total 
prices = [12.99, 5.50, 23.00, 10.25, 4.99]
total = 0 
i = 0 

while i < len(prices):
    total = total + prices[i]
    i = i + 1

print (total) 

# q1 countdown timer
countdown = 5 
while countdown > 0:
    print (countdown)
    countdown = countdown - 1 
print ("Blast off")

# q2 the even number hunter 
numbers = [11, 44, 23, 60, 37, 82]
i = 0 
while i < len(numbers):
    if numbers[i]% 2 == 0:
        print(numbers[i])
    i = i + 1

# q3 the multiplier 
numbers = [2, 5, 8, 10]
i = 0 
while i < len(numbers):
    newnum = numbers[i]*3
    print (newnum)

# q4 target finder 
scores = [45, 82, 68, 90, 70, 55]
i = 0 
while i < len(scores):
    if scores[i]>=70:
        print (scores[i])
    i = i + 1 

# q5 summing specific items 
prices = [4.50, 15.00, 8.25, 22.50, 3.00]
total = 0
i = 0
while prices[i] > 10:
    total = total + prices[i]
    i = i + 1 
    print (total)

# q6 discount finder 
prices = [45.00, 12.50, 60.00, 18.99, 5.00, 32.00]
i = 0

while i < len(prices):
    if prices[i] < 20:
        print (prices[i])
    i = i +1
