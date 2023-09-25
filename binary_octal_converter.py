import tkinter as tk

def binary_to_octal(binary_str):
    # Remove leading zeros and pad to a multiple of 3
    binary_str = binary_str.lstrip('0')
    length = len(binary_str)
    padding = (3 - (length % 3)) % 3
    binary_str = '0' * padding + binary_str

    octal_str = ""
    for i in range(0, len(binary_str), 3):
        octal_digit = binary_str[i:i + 3]
        octal_str += str(int(octal_digit, 2))

    return octal_str

def octal_to_binary(octal_str):
    binary_str = ""
    for octal_digit in octal_str:
        binary_digit = bin(int(octal_digit))[2:].zfill(3)
        binary_str += binary_digit

    return binary_str

def convert_binary_to_octal():
    binary_input = binary_entry.get()
    
    try:
        octal_result = binary_to_octal(binary_input)
        result_label.config(text=f"The octal equivalent is: {octal_result}")
    except ValueError:
        result_label.config(text="Invalid binary input. Please enter a valid binary number.")

def convert_octal_to_binary():
    octal_input = octal_entry.get()
    
    try:
        binary_result = octal_to_binary(octal_input)
        result_label.config(text=f"The binary equivalent is: {binary_result}")
    except ValueError:
        result_label.config(text="Invalid octal input. Please enter a valid octal number.")

# Create the main window
root = tk.Tk()
root.title("Binary and Octal Converter")

# Create and configure the binary input entry widget
binary_entry = tk.Entry(root)
binary_entry.pack(pady=10)

# Create a button to convert binary to octal
convert_binary_button = tk.Button(root, text="Convert Binary to Octal", command=convert_binary_to_octal)
convert_binary_button.pack()

# Create and configure the octal input entry widget
octal_entry = tk.Entry(root)
octal_entry.pack(pady=10)

# Create a button to convert octal to binary
convert_octal_button = tk.Button(root, text="Convert Octal to Binary", command=convert_octal_to_binary)
convert_octal_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", pady=10)
result_label.pack()

# Start the GUI event loop
root.mainloop()
