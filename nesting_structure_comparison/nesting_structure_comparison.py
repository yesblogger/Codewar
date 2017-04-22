"""
Created: 20/04/2017
Author: Amartya Gupta
"""


def same_structure_as(original, other):
    # checking if both are of type list
    if type(original) == list and type(other) == list:
        """
        cheking if both of them have the same len and initiate a recursion
        to check the whether the sub elements are of the same type and len.
        """
        if len(original) == len(other):
            for i, j in zip(original, other):
                if not same_structure_as(i, j):
                    return False
            else:
                return True
        else:
            return False
    else:
        # in case of non-equal types, both the elements have to be non-list
        if type(original) != list and type(other) != list:
            return True
        else:
            return False


print(same_structure_as([1, '[', ']'], ['[', ']', 1]))
