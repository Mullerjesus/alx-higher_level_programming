#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj: the object to be serialized to JSON

    Returns:
        A JSON string representing the input object
    """
    return json.dumps(my_obj)
