"""
Coding Challenge
"""

def question_1(input: str) -> str:
    """
    Given a string containing a sentence, reverse each word in place, and then
    return the result.

    Arguments:
        input {str} -- The string to reserve in place

    Returns:
        str -- The in place reserved string
    """

def question_2(hash1: dict, hash2: dict) -> dict:
    """
    Write a function that takes two hashes, merges them together, and returns the result. The hashes might contain integers, strings, arrays of integers, and other hashes (each of which might contain the same types of objects). When a duplicate key is found:

    * If the value is a string or integer, the value from the second hash should replace the value from the first
    * If the value is another hash, merge the two hashes together using these same rules.
    * If the value is an array, append the two arrays together.

    It's safe to assume that if a duplicate key is found, the values' type will be the same in both hashes.

    Arguments:
        hash1 {dict} -- Initial hash
        hash2 {dict} -- Update hash

    Returns:
        dict -- The updated hash
    """

def question_3(input: list) -> list:
    """
    Given an array of 100 numbers, many values are duplicates
    - find the duplicate values.

    Arguments:
        input {list} -- Array with duplicate values

    Returns:
        list -- The duplicate values found
    """

def question_4(cipher: list, message: list) -> str:
    """
    Given two linked lists, sort both lists by the first list alphabetically,
    and return the second list

    Arguments:
        cipher {list} -- The order the message should be sorted by
        message {list} -- The words to form the message with

    Returns:
        str -- The deciphered message
    """

def question_5(input: str) -> list:
    """
    Find all of the different permutations of a string, like “cats”, without
    using any built-in permutation functions

    Arguments:
        input {str} -- The word to permutate

    Returns:
        list -- A list of permutations
    """
