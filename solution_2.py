def rotated_array_search(input_list, number, mid=0):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array),
       number(int): Input array to search and the target
       mid:
    Returns:
       int: Index or -1
    """

    low = 0
    len_ = len(input_list)
    high = len_
    temp_ = None
    while low <= high:
        temp_ = (low + high) // 2
        if input_list[0] < input_list[len_ - 1] or temp_ == len_ - 1:
            temp_ = 0
            break
        if input_list[temp_ - 1] > input_list[temp_]:
            break
        elif input_list[0] < input_list[temp_]:
            low = temp_
        elif input_list[0] > input_list[temp_]:
            high = temp_

    if input_list[temp_] <= number <= input_list[len_ - 1]:
        low = temp_
        high = len_
    else:
        low = 0
        high = temp_

    while low <= high:
        temp_ = (low + high) // 2
        if input_list[temp_] == number:
            return temp_
        elif input_list[temp_] < number:
            low = temp_ + 1
        else:
            high = temp_ - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 6, 7, 8], 10])
