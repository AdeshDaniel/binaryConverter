import tkinter as tk

def binary_to_decimal(binary_str):
    decimal_num = 0
    length = len(binary_str)

    for i, digit in enumerate(binary_str[::-1]):  # Iterate through digits in reverse order
        if digit == '1':
            decimal_num += 2 ** i

    return decimal_num

def decimal_to_binary(decimal_num):
    binary_str = bin(decimal_num)[2:]  # Convert decimal to binary and remove '0b' prefix
    return binary_str

def convert_binary_to_decimal():
    binary_input = binary_entry.get()
    
    try:
        decimal_result = binary_to_decimal(binary_input)
        result_label.config(text=f"The decimal equivalent is: {decimal_result}")
    except ValueError:
        result_label.config(text="Invalid binary input. Please enter a valid binary number.")

def convert_decimal_to_binary():
    decimal_input = decimal_entry.get()
    
    try:
        decimal_input = int(decimal_input)
        binary_result = decimal_to_binary(decimal_input)
        result_label.config(text=f"The binary equivalent is: {binary_result}")
    except ValueError:
        result_label.config(text="Invalid decimal input. Please enter a valid decimal number.")

# Create the main window
root = tk.Tk()
root.title("Binary and Decimal Converter")

# Create and configure the binary input entry widget
binary_entry = tk.Entry(root)
binary_entry.pack(pady=10)

# Create a button to convert binary to decimal
convert_binary_button = tk.Button(root, text="Convert Binary to Decimal", command=convert_binary_to_decimal)
convert_binary_button.pack()

# Create and configure the decimal input entry widget
decimal_entry = tk.Entry(root)
decimal_entry.pack(pady=10)

# Create a button to convert decimal to binary
convert_decimal_button = tk.Button(root, text="Convert Decimal to Binary", command=convert_decimal_to_binary)
convert_decimal_button.pack()

# Create a label
result_label = tk.Label(root, text="", pady=10)
result_label.pack()

# start the GUI
root.mainloop()