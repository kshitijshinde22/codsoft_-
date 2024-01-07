import tkinter as tk
from tkinter import StringVar, IntVar
import random
import string

def generate_password():
    length = length_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if length < 1:
        result_var.set("Password length should be at least 1 character.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

root = tk.Tk()
root.title("Password Generator")

length_var = IntVar(value=12)
uppercase_var = IntVar(value=1)
digits_var = IntVar(value=1)
special_chars_var = IntVar(value=1)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root, textvariable=length_var, width=5, font=('Arial', 12), bd=5, relief=tk.GROOVE)
length_entry.grid(row=0, column=1, padx=10, pady=10)

uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var, font=('Arial', 12))
uppercase_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=('Arial', 12))
digits_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

special_chars_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var, font=('Arial', 12))
special_chars_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=('Arial', 14))
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_var = StringVar()
result_label = tk.Label(root, textvariable=result_var, font=('Arial', 14))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
