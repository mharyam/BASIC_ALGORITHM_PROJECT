def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # check for negative value and return ERROR
    if number < 0:
        return None
    #check for base case
    if (number == 0 or number == 1):
        return number

    start = 1
    end = number

    while (start <= end):
        mid_number = (start + end) // 2

        if mid_number * mid_number == number:
            return mid_number

        if mid_number * mid_number < number:
            start = mid_number + 1
            ans = mid_number
        else:
            end = mid_number -1
    return ans
#
#
print("Pass" if (3 == sqrt(9)) else "Fail")  # result should be 3
print("Pass" if (0 == sqrt(0)) else "Fail")  # result should be 0
print("Pass" if (4 == sqrt(16)) else "Fail")  # result should be 4
print("Pass" if (1 == sqrt(1)) else "Fail")  # result should be 1
print("Pass" if (5 == sqrt(27)) else "Fail")  # result should be 5
print("Pass" if (None == sqrt(-1)) else "Fail")  # result should be None
print("Pass" if (2236 == sqrt(5000000)) else "Fail")  # check for large value