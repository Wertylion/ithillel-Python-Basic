def is_even(number):
    even = [2,4,6,8,0]
    number = str(number)
    last_digit = number[-1]
    last_digit = int(last_digit)
    if last_digit in even:
        return True
    else:
        return False

    # def is_even(number):
    #     return int(str(number)[-1]) in [2, 4, 6, 8, 0]

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("OK")





