list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def List_prime(input_list):
    result_set = set()
    count_dict = {}

    for num in input_list:
        count = count_dict.get(num, 0) + 1
        count_dict[num] = count
        if count == 0:
            result_set.add(num)
        else:
            result_set.add(str(num) * count)
    return result_set


result_1 = List_prime(list_1)
result_2 = List_prime(list_2)
result_3 = List_prime(list_3)

print(result_1)
print(result_2)
print(result_3)
