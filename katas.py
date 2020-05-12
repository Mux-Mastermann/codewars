"""This file contains different solution functions from codewars challenges"""


def function_test():
    """Test functions here"""
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))


def dirReduc(arr):
    """kata: Directions Reduction

    Takes array of directions. Removes unneccessary oppositive directions next to each other
    """
    # creating compare lists
    horizontal = ["WEST", "EAST"]
    vertical = ["NORTH", "SOUTH"]
    # Remove indicator
    i = 0
    # creating slice of input arr
    while True:
        check = arr[i:i+2]
        if not check:
            return arr
        if check in [horizontal, horizontal[::-1], vertical, vertical[::-1]]:
            [arr.pop(i) for _ in range (2)]
            i = 0
            continue
        i += 1


def likes(names):
    """Kata: Who likes it?

    Takes Array of names. Returns Facebook like string telling who likes it
    """
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


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
