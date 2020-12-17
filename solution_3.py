def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    len_ = len(input_list)
    if len_ <= 1:
        return [-1, -1]

    input_frequency = [0] * 10
    for number in input_list:
        input_frequency[number] += 1

    list_1 = []
    list_2 = []
    first = 1
    if len_ % 2 != 0:
        first = 2
    for i in range(9, -1, -1):
        while input_frequency[i]:
            if first:
                list_1.append(str(i))
                first -= 1
            else:
                first += 1
                list_2.append(str(i))
            input_frequency[i] -= 1
    return [int(''.join(list_1)), int(''.join(list_2))]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])
test_function([[], [-1, -1]])
test_function([[0], [-1, -1]])
test_function([[0, 0], [0, 0]])
