def main():
    import math
    n = int(input("Enter a number: "))
    total=0
    for i in range(1,n):
        total += (-1)**(i+1)*((1.0/(i+i+1)))

    value = 4*(1-total)
    print(value)
    #subtracting
    xx = (math.pi - value)
    print('Lets see how close we are to pi:', xx)

main()
