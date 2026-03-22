def common_elements():
    list_numbers_1 = []
    for number_1 in range(100):
        if number_1 % 3 == 0:
            list_numbers_1.append(number_1)
    list_numbers_2 = []
    for number_2 in range(100):
        if number_2 % 5 == 0:
            list_numbers_2.append(number_2)
    set1 = set(list_numbers_1) & set(list_numbers_2)
    return set1

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')


# def common_elements():
#     list_numbers_1 = [number for number in range(100) if number % 3 == 0]
#     list_numbers_2 = [number for number in range(100) if number % 5 == 0]
#
#     result = set(list_numbers_1) & set(list_numbers_2)
#     return result
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print("OK")