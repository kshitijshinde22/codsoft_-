import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def clear_tasks():
    listbox.delete(0, tk.END)

def mark_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.itemconfig(selected_task_index, {'bg': 'light green'})

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30, font=('Arial', 14), bd=5, relief=tk.GROOVE)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

add_button = tk.Button(root, text="Add Task", command=add_task, font=('Arial', 12))
add_button.grid(row=0, column=2, padx=10, pady=10)

listbox = tk.Listbox(root, selectbackground='light blue', selectmode=tk.SINGLE, font=('Arial', 12), bd=5, relief=tk.GROOVE)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=('Arial', 12))
remove_button.grid(row=1, column=2, padx=10, pady=10, sticky=tk.NSEW)

mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, font=('Arial', 12))
mark_completed_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)

clear_button = tk.Button(root, text="Clear All", command=clear_tasks, font=('Arial', 12))
clear_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
