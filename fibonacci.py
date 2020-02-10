# 1 1 2 3 5 8 13
nn = int(input("Enter number "))

number1, number2 = 1, 1
count = 0

if nn <= 0:
    print("Enter first number")
elif nn == 1:
    print("Fibonacci sequence upto", nn, ":")
    print(number1)
else:
    print("Fibonacci sequence:")
    while count < nn:
        print(number1)
        nth = number1 + number2

        number1 = number2
        number2 = nth
        count += 1
