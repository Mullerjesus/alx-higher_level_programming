#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with 0s if they are too small
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Take only the first 2 elements of each tuple
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    # Add the elements together and return a new tuple
    return (a1 + b1, a2 + b2)
