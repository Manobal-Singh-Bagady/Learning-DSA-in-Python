while True:
    t = int(input())

    if t in range(1, 6):
        num1 = int(input())
        num2 = int(input())

        if t == 1:
            print(num1+num2)
        elif t == 2:
            print(num1-num2)
        elif t == 3:
            print(num1*num2)
        elif t == 4:
            print(num1//num2)
        elif t == 5:
            print(num1 % num2)

    elif t == 6:
        break

    else:
        print("Invalid Operation")
