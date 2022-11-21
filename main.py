a = int(input("enter range"))
while a >= 0:
    while True:
        for i in range(1, a + 1):
            print(a)
            a = a - 1
            if a == 0:
                b = (input("enter yes or no"))
                if b == "yes":
                    print(a)
                    a = a - 1
                    print ('-',i)
                    if a == 0:

                        break
                if b == "no":
                    break
