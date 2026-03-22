while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation (+ - * /): ")

    if operation == "+":
        print(first_number + second_number)

    elif operation == "-":
        print(first_number - second_number)

    elif operation == "*":
        print(first_number * second_number)

    elif operation == "/":
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("Division by zero is not allowed")

    else:
        print("Invalid operation")

    user_continue = input("Do you want to continue (y): ")
    if user_continue == "y":
        continue
    else:
        break
