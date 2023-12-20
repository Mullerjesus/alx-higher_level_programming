#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for val1, val2 in zip(my_list_1, my_list_2):
        try:
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)) and val2 != 0:
                result = val1 / val2
            elif val2 == 0:
                raise ZeroDivisionError("division by 0")
            else:
                raise TypeError("wrong type")
        except (ZeroDivisionError, TypeError) as e:
            print(e)
            new_list.append(0)  # Append 0 as a placeholder for the error
        else:
            new_list.append(result)
    return new_list
