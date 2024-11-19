def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    roman = roman.upper()
    integer_value = 0
    prev_value = 0

    for char in reversed(roman):
        if char in roman_values:
            value = roman_values[char]
            if value < prev_value:
                integer_value -= value
            else:
                integer_value += value
            prev_value = value
        else:
            return "Invalid Roman numeral"

    return integer_value

if __name__ == "__main__":
    roman_numeral = input("Enter a Roman numeral: ")
    result = roman_to_integer(roman_numeral)
    if isinstance(result, int):
        print(f"The integer value of '{roman_numeral.upper()}' is: {result}")
    else:
        print(result)