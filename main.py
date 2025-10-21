import re

def get_roman_input():
    try:
      roman = input("Enter a Roman numeral: ").upper()
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
        print("Error:", e)
        return None

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
    

    


# Main loop
if __name__ == "__main__":
    while True:
        roman_int = get_roman_input()
        if roman_int:
            roman_to_int(roman_int)
            print(f"The integer value is: {roman_to_int(roman_int)}")

        again = input("Do you want to convert another Roman numeral? (y/n): ").lower()
        if again != "y":
            print("Goodbye! 👋")
            break

