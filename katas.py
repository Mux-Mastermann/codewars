"""This file contains different solution functions from codewars challenges"""


def function_test():
    """Test functions here"""
    print(longest("aretheyhere", "yestheyarehere"))


def longest(s1, s2):
    """Kata: Two to One

    Take two strings of letters. Return a sorted string of distinct letters.
    """
    # combine the two strings into one
    s = s1 + s2
    # convert to a string of distinct letters
    s = set(s)
    print(s)
    s = list(s)
    print(s.sort())
    s = "".join(s)
    # sort the distinct string in alphabettical order
    
    return s

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
