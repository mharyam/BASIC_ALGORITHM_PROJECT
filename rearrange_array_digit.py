def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    odd_number = 0
    even_number = 0
    input_list.sort(reverse=True)

    # loop by odd
    for i in range(1, len(input_list), 2):
        odd_number = odd_number * 10 + input_list[i]

    #  loop by even
    for i in range(0, len(input_list), 2):
        even_number = even_number * 10 + input_list[i]

    return [odd_number, even_number]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])  # should print 573
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  # should print 1816
test_function([[4, 6, 2, 7, 9, 8], [974, 862]])  # should print 1836

#test with same number
test_function([[1, 1, 1, 1, 1], [111, 11]])

#test with empty array
test_function([[], []])

