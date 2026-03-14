# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True


import keyword
import string

variable_name = input("Enter variable name: ")

if not variable_name:
    print("Incorrect variable name: empty input")
elif keyword.iskeyword(variable_name):
    print(f"Incorrect variable name: {variable_name}")
elif "__" in variable_name:
    print(f"Incorrect variable name: {variable_name}")
elif any(symbol in string.punctuation.replace("_", "") for symbol in variable_name):
    print(f"Incorrect variable name: {variable_name}")
elif any(letter.isupper() for letter in variable_name):
    print(f"Incorrect variable name: {variable_name}")
elif variable_name[0].isnumeric():
    print(f"Incorrect variable name: {variable_name}")
else:
    print(f"Correct variable name: {variable_name}")