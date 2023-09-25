import tkinter as tk
import re

def is_binary(binary_str):
    # Use a regular expression to check if the input is a valid binary number
    return re.match(r'^[01]+$', binary_str) is not None

def binary_to_decimal(binary_str):
    decimal_num = 0
    length = len(binary_str)

    for i, digit in enumerate(binary_str[::-1]):  # Iterate through digits in reverse order
        if digit == '1':
            decimal_num += 2 ** i

    return decimal_num

def convert_binary_to_decimal():
    binary_input = binary_entry.get()
    
    if is_binary(binary_input):
        decimal_result = binary_to_decimal(binary_input)
        result_label.config(text=f"The decimal equivalent is: {decimal_result}")
    else:
        result_label.config(text="Invalid binary input. Please enter a valid binary number.")

# Create the main window
root = tk.Tk()
root.title("Binary to Decimal Converter")

# Create and configure the binary input entry widget
binary_entry = tk.Entry(root)
binary_entry.pack(pady=10)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_binary_to_decimal)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", pady=10)
result_label.pack()

# Start the GUI event loop
root.mainloop()
