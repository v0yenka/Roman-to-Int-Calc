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
  final_answer = 0
  # Handling the basic numerals first
  for i in numeral:
    if i == "M":
      final_answer += 1000
    elif i == "D":
      final_answer += 500
    elif i == "C":
      final_answer += 100
    elif i == "L":
      final_answer += 50
    elif i == "X":
      final_answer += 10
    elif i == "V":
      final_answer += 5
    elif i == "I":
      final_answer += 1

  # Now handling the special cases
  if "CM" in numeral:
    final_answer += 900
    numeral = numeral.replace("CM", "")
  if "CD" in numeral:
    final_answer += 400
    numeral = numeral.replace("CD", "")
  if "XC" in numeral:
    final_answer += 90
    numeral = numeral.replace("XC", "")
  if "XL" in numeral:
    final_answer += 40
    numeral = numeral.replace("XL", "")
  if "IX" in numeral:
    final_answer += 9
    numeral = numeral.replace("IX", "")
  if "IV" in numeral:
    final_answer += 4
    numeral = numeral.replace("IV", "")

  print("The roman numeral '" + roman_int + "' you entered translates to: " + str(final_answer) + "!")

# Main loop
if __name__ == "__main__":
    while True:
        roman_int = get_roman_input()
        if roman_int:
            roman_to_int(roman_int)

        again = input("Do you want to convert another Roman numeral? (y/n): ").lower()
        if again != "y":
            print("Goodbye! 👋")
            break

