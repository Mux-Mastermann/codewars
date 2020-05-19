"""This file contains different solution functions from codewars challenges"""


def function_test():
    """Test functions here"""
    print(list_squared(1, 50))


def list_squared(m, n):
    """Kata: Integers: Recreation One"""
    from math import sqrt
    results = []
    for i in range(m, n + 1):
        divisors = [x for x in range(1, i + 1) if i % x == 0]
        squared_divisors = [number * number for number in divisors]
        squared_divisors_sum = sum(squared_divisors)
        if sqrt(squared_divisors_sum) % 1 == 0:
            results.append([i, squared_divisors_sum]) 
    return results


def next_bigger(n):
    """Kata: Next bigger number with the same digits"""
    import itertools
    return min([int("".join(i)) for i in itertools.permutations(str(n)) if int("".join(i)) > n], default=-1)
    # works but doens't pass on codewars due to timeout. Not my bad.


def valid_parentheses(string):
    """Kata: Valid Parentheses"""
    for i, character in enumerate(string):
        if character == ")":
            if string[:i+1].count("(") < string[:i+1].count(")"):
                return False
        elif character == "(":
            if string[i:].count("(") > string[i:].count(")"):
                return False
    return True


def queue_time(customers, n):
    """Kata: The Supermarket Queue"""
    queues = [0 for _ in range(n)]
    for customer in customers:
        i = queues.index(min(queues))
        queues[i] += customer
    return max(queues)


def find_even_index(arr):
    """Kata: Equal Sides Of An Array"""
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return - 1


def order_weight(strng):
    """Kata: Weight for weight"""
    return " ".join(sorted(strng.split(), key=lambda string: (sum(int(i) for i in string), string)))


def find_outlier(integers):
    """kata: Find The Parity Outlier

    Input Array of integers. Only one integer is different. Either even or odd. Return this one
    """
    modulo_integers = [i % 2 for i in integers]
    n = 0 if modulo_integers.count(0) == 1 else 1
    return integers[modulo_integers.index(n)]


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
