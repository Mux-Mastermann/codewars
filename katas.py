"""This file contains different solution functions from codewars challenges for python"""
"""Test Commit"""

def function_test():
    """Test functions here"""
    print(halving_sum(25))


def halving_sum(n):
    """Kata: Halving Sum """
    x = n
    while n != 1:
        n = n // 2
        x = x + n
    return x


def rgb(r, g, b):
    """Kata: RGB To Hex Conversion"""
    results = []
    for x in [r, g, b]:
        if x < 0:
            x = 0
        elif x > 255:
            x = 255
        results.append(hex(x)[2:].zfill(2))
    return "".join(results).upper()



def josephus(items, k):
    """Kata: Josephus Permutation"""
    result = []
    index = 0
    while len(items) != 0:
        for _ in range(k):
            if index == len(items):
                index = 0
            index += 1
        result.append(items[index - 1])
        items.pop(index - 1)
        index -= 1
    return result


def list_squared(m, n):
    """Kata: Integers: Recreation One"""
    from math import sqrt
    results = []
    for i in range(m, n + 1):
        squared_divisors_sum = sum([x ** 2 for x in range(1, i + 1) if i % x == 0])
        if sqrt(squared_divisors_sum) % 1 == 0:
            results.append([i, squared_divisors_sum]) 


def is_solved(board):
    """Kata: Tic-Tac-Toe Checker"""
    board_list = [cell for line in board for cell in line]
    check_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for indices in check_indices:
        slice_set = set([board_list[i] for i in indices])
        if 0 in slice_set:
            continue
        if len(slice_set) == 1:
            return board_list[indices[0]]
    if 0 not in board_list:
        return 0
    return -1


def move_zeros(array):
    """Kata: Moving Zeros To The End"""
    result = []
    for element in array[::-1]:
        if element == 0 and element is not False:
            result.append(element)
        else:
            result.insert(0, element)
    return result


def anagrams(word, words):
    """Kata: Where my anagrams at?"""
    results = []
    dist_letter = [(letter, word.count(letter)) for letter in set(word)]
    for word in words:
        check_letter = [(letter, word.count(letter)) for letter in set(word)]
        if sorted(dist_letter, key=lambda x: x[0]) == sorted(check_letter, key=lambda x: x[0]):
            results.append(word)
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
