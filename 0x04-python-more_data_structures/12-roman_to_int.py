#!/usr/bin/python3
# 12-roman_to_int.py

def roman_to_int(roman_string):
    """converts a roman numeral to an integer"""
    numeral_map = {
            "i": 1, "v": 5,
            "x": 10, "l": 50,
            "c": 100, "d": 500,
            "m": 1000}
    integers = [0]
    # Check if roman_string is a string and not None
    if (not roman_string) or (not isinstance(roman_string, str)):
        return 0
    i = 0
    while i < len(roman_string):
        char = roman_string[i].lower()
        if char not in numeral_map.keys():
            return 0
        # check if there is a next
        if (i + 1) < len(roman_string):
            next_char = roman_string[i + 1].lower()
            if next_char not in numeral_map.keys():
                return 0
            if numeral_map[char] >= numeral_map[next_char]:
                integer = numeral_map[char]
                integers.append(integer)
            else:
                integer = numeral_map[next_char] - numeral_map[char]
                integers.append(integer)
                i += 2
                continue
        else:
            integer = numeral_map[char]
            integers.append(integer)
        i += 1
    return sum(integers)
