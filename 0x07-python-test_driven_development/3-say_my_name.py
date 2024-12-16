#!/usr/bin/python3
"""
say_my_name module.

This module provides a function for generating a full name string.

Functions:
    say_my_name(firt_name, last_name="") -> str:\
        Generate a string with the full name.
"""


def say_my_name(first_name, last_name="") -> str:
    """
    Return a string with the full name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Returns:
        str: A string in the format "My name is {first_name} {last_name}"

    Raises:
        TypeError: if `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # full_name = "My name is"
    # if first_name:
    #     full_name += " " + first_name
    # if last_name:
    #     full_name += " " + last_name
    print("My name is {} {}".format(first_name, last_name))
