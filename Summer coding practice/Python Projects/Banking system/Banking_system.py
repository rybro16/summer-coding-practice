import tkinter as tk 
from tkinter import messagebox, simpledialog
import json
import os

window = tk.Tk()
window.title("Banking system")
window.geometry("400x300")
window.resizable(False, False)
login_frame = tk.Frame(window)
register_frame = tk.Frame(window)
account_frame = tk.Frame(window)
current_balance = 0.0

welcome_label = tk.Label(
    account_frame,
    text = "",
    font = ("Arial", 18)
)
welcome_label.pack()

balance_label = tk.Label(
    account_frame,
    text = "Balance: £ 0.00",
    font=("Arial", 14)
)
balance_label.pack()

def deposit():

    global current_balance

    amount = simpledialog.askfloat(
        "Deposit",
        "Enter amount to deposit"
    )

    current_balance = current_balance + amount

    balance_label.config(
        text = f"Balance: £ {current_balance:.2f}"
    )

def withdraw():
    global current_balance
    amount = simpledialog.askfloat(
        "Withdraw",
        "Enter amount to withdraw"
    )

    if amount is None:
        return

    if amount <= 0:
        messagebox.showerror(
            "Withdraw error",
            "Please enter a valid amount"
        )
        return

    if amount > current_balance:
        messagebox.showerror(
            "Withdraw error",
            "Insufficient funds"
        )
        return

    current_balance = current_balance - amount

    balance_label.config(
        text = f"Balance: £ {current_balance:.2f}"
    )
    
deposit_button = tk.Button(
    account_frame,
    text = "Deposit",
    font = ("Arial", 12),
    command = deposit
)
deposit_button.pack()

withdraw_button = tk.Button(
    account_frame,
    text = "Withdraw",
    font = ("Arial", 12),
    command = withdraw
)
withdraw_button.pack()

title_label = tk.Label(login_frame, 
                       font = ("Arial", 18),
                       text = "Welcome to the Bank")
title_label.pack()

# username box

# This says: when the box is clicked, check whether it still contains “Enter username.” 
# If it does, delete it and change the typing colour to black.
def clear_username_placeholder(event):
    if username_entry.get() == "Enter username":
        username_entry.delete(0, tk.END)
        username_entry.config(fg = "black")

# creates username textbox
username_entry = tk.Entry(login_frame)
username_entry.pack() # shows it on the window

username_entry.insert(0, "Enter username")
username_entry.config(fg = "grey")

username_entry.bind("<FocusIn>", clear_username_placeholder)

# password box 

def clear_password_placeholder(event):
    if password_entry.get() == "Enter password":
        password_entry.delete(0, tk.END)
        password_entry.config(fg = "black")

password_entry = tk.Entry(login_frame)
password_entry.pack()

password_entry.insert(0, "Enter password")
password_entry.config(fg = "grey")

password_entry.bind("<FocusIn>", clear_password_placeholder)

# log in box 
login_button = tk.Button(
    login_frame,
    text = "Log in",
    bg="#1F4E79",
    fg="white",
    font = ("Arial", 12, "underline")
)
login_button.pack()

def show_register_page():
    login_frame.pack_forget()
    register_frame.pack(fill = "both", expand = True)

def show_login_page():
    register_frame.pack_forget()
    login_frame.pack(fill = "both", expand = True)


def show_account_page(username, balance):
    login_frame.pack_forget()

    welcome_label.config(text = f"Welcome, {username}")
    balance_label.config(text = f"Balance: £ {balance:.2f}")

    account_frame.pack(fill = "both", expand = True)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            accounts = json.load(file)

        if isinstance(accounts, dict):
            if accounts:
                accounts = [accounts]
            else:
                accounts = []
    else:
        messagebox.showerror("Login error", "No accounts have been created yet")
        return

    for account in accounts:
        if account["username"] == username and account["password"] == password:
            global current_balance
            current_balance = account.get("balance", 0.0)
            show_account_page(username, current_balance)
            return

    messagebox.showerror(
        "Login error",
        "Incorrect username or password"
    )

login_button.config(command = login)

# register/ create acount box
register_button = tk.Button(
    login_frame,
    text = "Register / Create Account",
    font = ("Arial", 12, "underline"),
    command = show_register_page
)

register_button.pack()

register_title_label = tk.Label(
    register_frame,
    text = "Create an Account",
    font = ("Arial", 18)
)
register_title_label.pack()

email_label = tk.Label(
    register_frame,
    text = "Email"
)
email_label.pack()

email_entry = tk.Entry(register_frame)
email_entry.pack()

username_label = tk.Label(
    register_frame,
    text = "Username"
)
username_label.pack()

register_username_entry = tk.Entry(register_frame)
register_username_entry.pack()

password_label = tk.Label(
    register_frame,
    text = "Password"
)
password_label.pack()

register_password_entry = tk.Entry(
    register_frame,
    show = "*"
)
register_password_entry.pack()

confirm_password_label = tk.Label(
    register_frame,
    text = "Confirm Password"
)
confirm_password_label.pack()

confirm_password_entry = tk.Entry(
    register_frame,
    show = "*"
)
confirm_password_entry.pack()

def create_account():
    password = register_password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()
    username = register_username_entry.get()

    if os.path.exists("accounts.json"):
        with open("accounts.json", "r")as file:
            accounts = json.load(file)

        if isinstance(accounts, dict):
            if accounts:
                accounts = [accounts]
            else:
                accounts = []

    else:
        accounts = []

    for saved_account in accounts:
        if saved_account["email"] == email:
            messagebox.showerror(
                "Account already exists",
                "An account already exists with this email. Please log in"
            )
            show_login_page()
            return

        if saved_account["username"] == username:
            messagebox.showerror(
                "Username taken",
                "That username is already taken. PLease choose another."
            )
            return
        
    if password == confirm_password:
        account = {
            "email": email,
            "username": username,
            "password": password,
            "balance": 0.0
        }

        accounts.append(account)

        with open("accounts.json", "w") as file:
            json.dump(accounts, file)
        messagebox.showinfo("Account created", "Account created successfully")
        show_login_page()
    else:
        messagebox.showerror("Password error", "Passwords do not match")
    

create_account_button = tk.Button(
    register_frame,
    text = "Create Account",
    command = create_account 
)
create_account_button.pack()

login_frame.pack(fill = "both", expand = True)


window.mainloop()


