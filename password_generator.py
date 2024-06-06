import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_special_chars = special_chars_var.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, pady=5)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, columnspan=2, pady=5)

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, columnspan=2, pady=5)

special_chars_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var).grid(row=3, columnspan=2, pady=5)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, columnspan=2, pady=5)

# Run the application
root.mainloop()
