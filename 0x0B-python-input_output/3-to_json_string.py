#!/usr/bin/python3
"""
Contains the "from_json_string" function
"""

import json

def from_json_string(json_string):
    """
    Returns an object represented by a JSON string.

    Args:
        json_string: the JSON string to be deserialized

    Returns:
        The deserialized object from the input JSON string
    """
    return json.loads(json_string)
