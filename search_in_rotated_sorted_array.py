def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return recursive_binary_search(number, input_list)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def recursive_binary_search(target, source):
    if len(source) == 0:
        return None
    left = 0
    right = len(source)-1

    while left <= right:
        middle = (left + right)//2

        if source[middle] == target:
            return middle

        if source[middle] >= source[left]:
            if source[middle] >= target >= source[left]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if source[middle] >= target <= source[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # should print 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # should print 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])  # should print 2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])  # should print 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # should print -1

""" corner test cases  """
#test with an normal sorted  array
test_function([[1, 2, 3, 4, 5, 6, 7], 10])  # should print -1
#test with an unsorted arry
test_function([[1, 5, 2, 3, 10, 4, 12], 5])  # should FAIL because it is unsorted



