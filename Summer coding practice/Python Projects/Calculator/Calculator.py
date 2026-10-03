num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
def plus():
    return num1 + num2
def minus():
    return num1 - num2
def multiply():
    return num1 * num2
def divide():
    return num1 / num2
print("Operators: ")
print("1 = plus")
print("2 = minus")
print("3 = multiply")
print("4 = divide")

operator = 0 
while operator > 4 or operator < 1:

    operator = int(input("Enter your operation (numbers between 1-4): "))
    if operator < 1 or operator > 4:
        print("Invalid option")
if operator == 1:
    answer = plus()
elif operator == 2:
    answer = minus()
elif operator == 3:
    answer = multiply()
elif operator == 4:
    answer = divide()
else: 
    print("Invalid option")
print(answer)