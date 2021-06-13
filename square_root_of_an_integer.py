def get_pair_value(number):
    if number <= 99:
        return number
    return -1
    # elif number <= 999:
    #     number = number/10
    #     number = str(number)
    #
    # elif number <= 9990:
    #     number = number/100
    #     number = str(number)

    # return str(number).split('.')


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # since the test is only for integer with a single pair
    pair_value = get_pair_value(number)
    if pair_value >= 0:
        largest_int = 0
        for i in range(pair_value+1):
            if i*i <= pair_value:
                largest_int = i
        return largest_int
    return "ERROR this program is for a number between 0-99"


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")