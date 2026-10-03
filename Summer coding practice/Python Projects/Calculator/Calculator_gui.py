import tkinter as tk
# Creates the main calculator window.
window = tk.Tk() 
window.title("Calculator")
# Makes the window background dark blue.
window.configure(bg = "#1f2937")
# creates like a textbox
display = tk.Entry(window, width = 20, font=("Arial", 22)) 
# this puts the box in the window and Places the display in row 0, column 0,
#and makes it stretch across 4 columns.
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10) 

# This function adds a clicked number or symbol to the display.
def button_click(value): 
    display.insert(tk.END, value)

# Clears everything currently shown in the display.
def clear():
    display.delete(0, tk.END)

# This function runs when "=" is clicked.
def calculate():
    # try means: attempt to run this code.
    # If it works, show the answer.
    try:
        answer = eval(display.get()) # Gets the text from the display and works out the calculation.
        display.delete(0, tk.END) # Clears the old calculation from the display.
        display.insert(0, answer)# Shows the answer in the display.

# except ZeroDivisionError runs if someone tries 5/0 or 0/0.
    except ZeroDivisionError:
        display.delete(0,tk.END)
        display.insert(0, "Cannot divide by zero")


# This list controls the buttons and the order they appear in.
buttons = [
    "C", "7", "8", "9",
    "+", "4", "5", "6",
    "-", "1", "2", "3",
    "*", "0", ".", "=",
    "/"
]

# Starts button placement in the first row below the display,
# at the left-most column.
row = 1
column = 0

# Repeats once for every item in the buttons list.
for number in buttons:
    # Makes the Clear button.
    if number =="C":
        button = tk.Button(
            window,
            text=number,
            font=("Arial", 18),
            width=5,
            height=2,
            bg="#ef4444",
            command=clear
        )

    # Makes the equals button.
    elif number == "=":
        button = tk.Button(
            window,
            text = number,
            font = ("Arial, 18"),
            width = 5,
            height = 2,
            bg = "#f59e0b",
            command = calculate
        )

    # Otherwise, make a normal button that adds its character
    # to the display when clicked.
    else:
        button = tk.Button(
            window, 
            text = number, 
            font=("Arial", 18),
            width=5,
            height=2,
            bg="#e5e7eb",
            command = lambda n = number: button_click(n))

    # Places the button in its current row and column.
    button.grid(row = row, column = column, padx=4, pady=4)
    # Moves to the next column for the next button.
    column = column + 1

# Once 4 columns have been used, return to column 0
# and move down one row.
    if column == 4:
        column = 0
        row = row + 1

# Keeps the window open and waiting for button clicks.
window.mainloop()

