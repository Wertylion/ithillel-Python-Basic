# V1
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
# V2
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
