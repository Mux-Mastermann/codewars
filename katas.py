"""This file contains different solution functions from codewars challenges"""


def function_test():
    """Test functions here"""
    print(array_diff([1,2,2,2,3],[2]))


def array_diff(a, b):
    """Kata: Array.diff

    Takes two lists. Removes all values from list a, that are in list b.
    """
    return [item for item in a if item not in b]


def longest(s1, s2):
    """Kata: Two to One

    Take two strings of letters. Return a sorted string of distinct letters.
    """
    # combine the two strings, make a set of unique chars, then make a list
    s = list(set(s1 + s2))
    # sort unique char list
    s.sort()
    return "".join(s)


def friend(input_list):
    """Kata: Friend or Foe?

    Takes list, filters out only strings with 4 letters
    """
    # create a new list for the output
    friends = []
    # loop through input list
    for element in input_list:
        # has element 4 letters?
        if len(element) == 4:
            # append element to a new list
            friends.append(element)
    # return new list
    return friends


def alphabet_position(text):
    """Kata: Replace With Alphabet Position

    Give a string, replace every letter with position in alphabet
    """
    import string
    new_str = []
    for char in text:
        if not char.isalpha():
            continue
        new_str.append(str(string.ascii_lowercase.index(char.lower()) + 1))
    return " ".join(new_str)


if __name__ == "__main__":
    function_test()
