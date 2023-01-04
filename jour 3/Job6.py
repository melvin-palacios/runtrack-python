from random import randint


def job6(nb):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    j = 0
    index = 0

    while i <= nb:
        while j <= i:
            if index == 26:
                index = 0
            color = randint(31, 37)
            print(f"\033[0;{color};40m {alphabet[index]}", end='')
            j+=1
            index+=1
        print(' ')
        j = 0
        i+=1


job6(15)
