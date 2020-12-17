def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number ** 2 == number:
        return number
    low = 0
    high = number
    while low <= high:
        middle = (low + high) // 2
        if (middle ** 2 == number) or (middle ** 2 <= number < (middle + 1) ** 2):
            return middle
        elif middle ** 2 > number:
            high = middle
        else:
            low = middle


print("Pass" if (3 == sqrt(9)) else "Fail")  # Pass
print("Pass" if (0 == sqrt(0)) else "Fail")  # Pass
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
