"""
Coding Challenge
"""

import copy

__all__ = []

for i in range(1, 6):
    __all__.append(f"question_{i}")


def question_1(input: str) -> str:
    """
    Given a string containing a sentence, reverse each word in place, and then
    return the result.

    Arguments:
        input {str} -- The string to reserve in place

    Returns:
        str -- The in place reserved string
    """
    punctuation = ["?", ",", ".", ":", ";", "!"]

    words = input.split(" ")
    for i in range(len(words)):
        if words[i][-1] in punctuation:
            words[i] = (
                words[i][-1] + words[i][:-1]
            )  # Flip location of ending punctuation so it stays there
    reversed_words = [x[::-1] for x in words]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


def question_2(hash1: dict, hash2: dict) -> dict:
    """
    Write a function that takes two hashes, merges them together, and returns the result. The hashes might contain integers,
    strings, arrays of integers, and other hashes (each of which might contain the same types of objects).
    When a duplicate key is found:

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
    ans = {}  # Create new dictionary to store answer to avoid modifying the inputs
    for key, u_val in hash2.items():
        if key not in hash1:
            ans[key] = u_val
        else:
            if type(u_val) == list:
                ans[key] = hash1[key] + u_val
            elif type(u_val) == dict:
                ans[key] = question_2(hash1[key], u_val)
            else:
                ans[key] = u_val

    for key, i_val in hash1.items():
        if key not in ans:
            ans[key] = i_val
    return ans


def question_3(input: list) -> list:
    """
    Given an array of 100 numbers, many values are duplicates
    - find the duplicate values.

    Arguments:
        input {list} -- Array with duplicate values

    Returns:
        list -- The duplicate values found
    """

    found_words = set()
    ans = set()
    for word in input:
        if word in found_words:
            ans.add(word)
        else:
            found_words.add(word)
    return list(ans)


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

    # looked up sorted syntax here https://docs.python.org/3/library/functions.html#sorted

    combined = zip(cipher, message)
    combined = sorted(combined, key=lambda x: x[0])
    sorted_message = " ".join([x[1] for x in combined])

    return sorted_message


def get_permutations(input: str, current: str, ans: list) -> list:
    """Generates all permutations from input and concats value in current to the end.
    These are then placed in ans.

    Args:
        input (str): String to create permutations from
        current (str): value to concatonate to the end of each permutation of input
        ans (list): Contains all previously created permutation combinations

    Returns:
        list: Combination of previously created Permutation combinations and newly created combos
    """
    if len(input) == 0:
        ans.append(current)

    for i in range(len(input)):
        holdout = input[i]
        left = input[:i]
        right = input[i + 1 :]
        lr = left + right
        get_permutations(lr, holdout + current, ans)
    return ans


def question_5(input: str) -> list:
    """
    Find all of the different permutations of a string, like “cats”, without
    using any built-in permutation functions

    Arguments:
        input {str} -- The word to permutate

    Returns:
        list -- A list of permutations
    """
    return get_permutations(input, "", [])


if __name__ == "__main__":
    print(question_5("a"))
