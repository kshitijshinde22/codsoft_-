import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4)

# Define button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to the grid
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 14),
              command=lambda value=button: on_button_click(value) if value != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', width=5, height=2, font=('Arial', 14), command=clear_entry).grid(row=row_val, column=col_val)

root.mainloop()



   