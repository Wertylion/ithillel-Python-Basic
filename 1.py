# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)
# print(magicians)
#
# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)
#
# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)
#
# squares = [value**2 for value in range(1,11)]
# print(squares)
#
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# film_rating = int(input("Enter film rating: "))
#
# if 0 < film_rating <= 5:  # film_rating > 0 and film_rating <= 5
#     if 4 <= film_rating < 6:
#         print("Film OK!")
#     else:
#         print("Film not OK!")
# else:
#     print("Incorrect Rating!")


# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# operation = input("Enter operation (+ - * /): ")
#
# if operation == "+":
#     print(first_number + second_number)
#
# elif operation == "-":
#     print(first_number - second_number)
#
# elif operation == "*":
#     print(first_number * second_number)
#
# elif operation == "/":
#     if second_number != 0:
#         print(first_number / second_number)
#     else:
#         print("Division by zero is not allowed")
#
# else:
#     print("Invalid operation")



# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# operation = input("Enter operation (+ - * /): ")
#
# match operation:
#     case "+":
#         print(first_number + second_number)
#     case "*":
#         print(first_number * second_number)
#     case "-":
#         print(first_number - second_number)
#     case "/":
#         if second_number != 0:
#             print(first_number / second_number)
#         else:
#             print("Division by zero is not allowed")
#     case _:
#         print("Invalid operation")

# first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2]
# print(first_list.index(5)) # 2
# # Пошук наступного значення
# print(first_list.index(5, 3))  # 4
# print(first_list.index(5, 5))  #  6


# a = int(input("Input a "))
# b = int(input("Input b "))
# i = 0
# while i < a: # Висота
#     j = 0
#     while j < b: # ширина
#         print("*", end='') # рядок не буде переведено
#         j += 1
#     print()
#     i += 1

# first_list = [[1, 2, 3], [4, 5, 6]]
# i = 0
# print(first_list)
# while i < len(first_list):
#     j = 0
#     lst = first_list[i]
#     while j < len(lst):
#         print(lst[j])
#         j += 1
#     i += 1
#
# first_list = [[1, 2, 3], [4, 5, 6]]
# for lst in first_list:
#     for num in lst:
#         print(num)

# import random
# my_list = []
# # Не найоптимальніший варіант рішення
# for i in range(random.randint(6, 15)):
#     my_list.append(random.randint(1, 100))
# print(my_list)
#
# summa = 0
# for element in my_list:
#     summa += element
# print(summa)
#
# # варіант створення списків за допомогою генератора списків (спискове включення)
# my_list = [random.randint(1, 100) for i in range(random.randint(6, 15))]
# print(my_list)
#
# # Знаходження суми елементів послідовності за допомогою вбудованої функції sum
# print(sum(my_list))
#
# # оптимальний варіант рішення
# my_list = [random.randint(1,100) for i in range(random.randint(6, 15))]
# print(my_list)
# print(sum(my_list))

# name = "dima"
# name = "D" + name[1:]
# name = name + "."
# print(name)

# numbers = list(range(100))
# print(numbers)
# list_numbers = []
# for number_1 in numbers:
#     if number_1 % 3 == 0 and number_1 % 5 == 0:
#         list_numbers.append(number_1)
#         print(list_numbers)

# №№№№№№№№№№№№№№№№№№№№№№№№#

# numbers = int(input("n = "))
# list_1 = []
# for i  in range(numbers + 1):
#     if i % 2 == 0:
#         list_1.append(i)
# print(list_1)


# list_2= []
# for i in range(100):
#     if i % 3 == 0:
#         list_2.append(i)
# print(list_2)

# hello → olleh
# python → nohtyp

# lesson = input(":")
# print(lesson[::-1])
#
# def reverse_string(text):
#     return text[::-1]
#
#
# word = input("Enter text: ")
# print(reverse_string(word))

# word = input("Enter text: ")
# set_1 = {}
# for i in word:
#     if i in set_1:
#         set_1[i] += 1
#     else:
#         set_1[i] = 1
#
# print(set_1)
#
# [1, 5, 3, 9, 7] → 7
# [10, 20, 30] → 20

# numbers = [10, 20, 30]
# print(sorted(set(numbers))[-2])

# set_nums_1 = [1, 2, 3, 4]
# set_nums_2 = [3, 4, 5, 6]
# set_nums_3 = []
# for i in set_nums_1:
#     for j in set_nums_2:
#         if i == j:
#             set_nums_3.append(i)
# print(set_nums_3)
#
# set_nums_1 = [1, 2, 3, 4]
# set_nums_2 = [3, 4, 5, 6]
# set_nums_3 = []
# for i in set_nums_1:
#     if i in set_nums_2:
#         set_nums_3.append(i)
# print(set_nums_3)
# list_1 = [1, 2, 3, 4]
# list_2 = [3, 4, 5, 6]
#
# result = list(set(list_1) & set(list_2))

print(result)



