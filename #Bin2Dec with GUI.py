import tkinter as tk
from tkinter import messagebox

def convert_binary_to_decimal():
    # Get user input from the entry widget
    user_input = binary_entry.get()
    total = 0

    # Presence Check
    if not user_input:
        messagebox.showerror("Error", "The input cannot be empty. Please input a 1 - 8 bit binary digits: ")
        return

    # Validity Check
    if not all(bit in "01" for bit in user_input):
        messagebox.showerror("Error", "The app can only convert binary digits. Please input a 1 - 8 bit binary digits: ")
        return

    # Convert input into an array
    binary_input_array = list(user_input)
    array_size = len(binary_input_array)

    # Flip the array
    binary_input_array.reverse()

    # Program Logic
    for i in range(0, array_size):
        if binary_input_array[i] == '1':
            total += 2**i
        else:
            total += 0

    # Display the result in a messagebox
    messagebox.showinfo("Result", f"The equivalent denary equivalent for {user_input} is {total}")

# Create the main window
root = tk.Tk()
root.title("Binary to Decimal Converter")

# Create and place widgets
binary_label = tk.Label(root, text="Enter 1 - 8 bit binary digits:")
binary_label.pack()

binary_entry = tk.Entry(root)
binary_entry.pack()

convert_button = tk.Button(root, text="Convert", command=convert_binary_to_decimal)
convert_button.pack()

# Start the GUI event loop
root.mainloop()
