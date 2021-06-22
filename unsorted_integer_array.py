def get_min_max(ints):
    """
    In this problem, we will look for smallest and largest integer from a list of unsorted integers.
    The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return []
    max_num = ints[0]
    min_num = ints[0]
    for value in ints:
        if max_num > value:
            max_num = value
        if min_num < value:
            min_num = value
    return max_num, min_num


## Example Test Case of Ten Integers


# import random
#
# l = [i for i in range(0, 10)]  # a list containing 0 - 9
# random.shuffle(l)


def test_function(*args):
    # min_max_range = [i for i in range(0, args[2])]
    print("Pass" if ((args[0], args[1]) == get_min_max(args[2])) else "Fail")


test_function(0, 9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # should print (0, 9)
test_function(1, 100, [100, 1, 2, 3, 4, 5, 6, 7, 8, 90])  # should print (0, 19)
test_function(0, 4, [0, 1, 2, 3, 4])  # should print (0, 4)
test_function(0, 0, [0])

test_function(1, 20, [2, 1, 3, 20, 10])
test_function(0, 0, []) # this will fail
test_function(-1, 50, [-1, 50, 20, 0]) # this will fail
