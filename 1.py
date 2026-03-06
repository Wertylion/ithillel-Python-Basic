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



first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation (+ - * /): ")

match operation:
    case "+":
        print(first_number + second_number)
    case "*":
        print(first_number * second_number)
    case "-":
        print(first_number - second_number)
    case "/":
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("Division by zero is not allowed")
    case _:
        print("Invalid operation")
