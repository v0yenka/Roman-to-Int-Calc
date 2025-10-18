import tkinter as tk
from tkinter import PhotoImage
import re

# Logic functions
def validate_roman_input(roman_input):
    try:
        roman = roman_input.upper()

        # Checking only letters
        if not roman.isalpha():
            raise ValueError("Roman numerals must contain only letters (I, V, X, L, C, D, M).")

        # Validating Roman characters
        valid_chars = set("IVXLCDM")
        if not all(ch in valid_chars for ch in roman):
            raise ValueError("Invalid character in Roman numeral.")

        # Validating Roman numeral structure
        roman_pattern = re.compile(
            r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
        )
        if not roman_pattern.match(roman):
            raise ValueError("Invalid Roman numeral structure.")

        return roman
    except ValueError as e:
        return str(e)

def roman_to_int(numeral):
    # Convert a valid Roman numeral to an integer
    # Tried to optimize with a dictionary and loop
    numeral = numeral.upper()
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    special_cases = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    total = 0
    i = 0

    # Looping through the numeral
    while i < len(numeral):
        # Fixed the special case handling
        # Checking if a special case (like IV or IX) starts at position i
        if i + 1 < len(numeral) and numeral[i:i+2] in special_cases:
            total += special_cases[numeral[i:i+2]]
            i += 2
        else:
            total += values[numeral[i]]
            i += 1

    return total

# GUI functions
def convert():
    roman_input = entry.get()
    validation_result = validate_roman_input(roman_input)

    if "Invalid" in validation_result or "must contain" in validation_result or "Error" in validation_result:
        result_label.config(text=f"Error: {validation_result}")
    else:
        value = roman_to_int(validation_result)
        result_label.config(text=f"The Roman numeral '{validation_result}' you entered translates to {value}!")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Roman Numeral Calculator GUI")
root.geometry("600x450")
root.configure(bg="pink")

# Custom icon (optional)
try:
    icon = PhotoImage(file="my_icon.png")
    root.iconphoto(True, icon)
except Exception:
    pass  # if icon not found

tk.Label(root, text="Enter a Roman numeral:", fg="white", bg="pink",
         font=("Lucida Handwriting", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, font=("Lucida Handwriting", 16), justify="center")
entry.pack(pady=10)

tk.Button(root, text="Convert", font=("Lucida Handwriting", 14, "bold"),
          fg="white", bg="purple", width=12, command=convert).pack(pady=5)
tk.Button(root, text="Clear", font=("Lucida Handwriting", 14, "bold"),
          fg="white", bg="purple", width=12, command=clear).pack(pady=5)

result_label = tk.Label(root, text="", fg="white", bg="pink",
                        font=("Lucida Handwriting", 14))
result_label.pack(pady=10)

root.mainloop()