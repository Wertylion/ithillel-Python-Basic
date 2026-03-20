# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA


import string

user_input = input("Enter two letters separated by a hyphen, for example a-c: ")

start, end = user_input.split("-")

letters = string.ascii_letters

start_index = letters.index(start)
end_index = letters.index(end)

if start_index <= end_index:
    result = ""
    for i in range(start_index, end_index + 1):
        result += letters[i]
else:
    result = ""
    for i in range(start_index, end_index - 1, -1):
        result += letters[i]

print(result)
