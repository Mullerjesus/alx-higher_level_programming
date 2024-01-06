#!/usr/bin/python3
def __setattr__(self, key, value):
    if not hasattr(self, key) and key != 'first_name':
        raise AttributeError("Cannot create new instance attribute")
    super().__setattr__(key, value)
