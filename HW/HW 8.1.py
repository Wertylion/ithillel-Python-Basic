def add_one(some_list):
    result = 0

    for digit in some_list:
        result = result * 10 + digit
    result += 1

    digits = []
    for x in str(result):
        digits.append(int(x))

    return digits

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")