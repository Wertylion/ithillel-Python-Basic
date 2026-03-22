num = int(input("Enter number: "))

while num > 9:
    mult = 1

    for i in str(num):
        mult = mult * int(i)

    num = mult

print(num)