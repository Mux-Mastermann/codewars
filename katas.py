"""This file contains different solution functions from codewars challenges"""


def function_test():
    """Test functions here"""
    print(likes([]))


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
