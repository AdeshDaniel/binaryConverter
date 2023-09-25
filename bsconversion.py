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

def main():
    binary_input = input("Enter a binary number: ")
    
    if is_binary(binary_input):
        decimal_result = binary_to_decimal(binary_input)
        print(f"The decimal equivalent is: {decimal_result}")
    else:
        print("Invalid binary input. Please enter a valid binary number.")

if __name__ == "__main__":
    main()
