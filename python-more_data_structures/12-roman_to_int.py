#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    previous_value = 0

    for c in reversed(roman_string):
        if c not in roman_to_int_map:
            return 0

        value = roman_to_int_map[c]

        if value < previous_value:
            total -= value
        else:
            total += value

        previous_value = value

    return total
