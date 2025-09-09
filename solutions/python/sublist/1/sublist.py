"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    l1 = len(list_one)
    l2 = len(list_two)
    if list_one == list_two:
        return EQUAL
    if l1 < l2:
        for i in range(l2-l1+1):
            if list_one == list_two[i:i+l1]:
                return SUBLIST
    if l1 > l2:
        for i in range(l1-l2+1):
            if list_two == list_one[i:i+l2]:
                return SUPERLIST
    return UNEQUAL