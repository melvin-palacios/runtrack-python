def job3(nb):
    i = 0
    print("+", end="")
    print((nb + 1) * "-", end="")
    print("+")

    while i < nb:
        print("|", end="")
        print((nb - i) * "#", end="")
        print(' ', end="")
        print(i*"#",end="")
        print("|")
        i+=1


    print("+", end="")
    print((nb + 1) * "-", end="")
    print("+")

job3(10)