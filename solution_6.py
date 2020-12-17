import random


def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return

    answer = [-float('inf'), float('inf')]
    for number in ints:
        if number > answer[0]:
            answer[0] = number
        if number < answer[1]:
            answer[1] = number
    return answer[1], answer[0]


# Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")
print("Pass" if ((0, 0) == get_min_max_by_sorting([0])) else "Fail")
print("Pass" if (None == get_min_max_by_sorting([])) else "Fail")
