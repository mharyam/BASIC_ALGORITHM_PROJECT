def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_num = 0
    min_num = 0
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
    min_max_range = [i for i in range(0, args[2])]
    print("Pass" if ((args[0], args[1]) == get_min_max(min_max_range)) else "Fail")


test_function(0, 9, 10)  # should print (0,9)
test_function(0, 19, 20)  # should print (0,19)
test_function(0, 4, 5)  # should print (0,4)
