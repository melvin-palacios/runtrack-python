from random import randint
def Job5():
    i = 2
    while i < 1001:
        for a in range(2, i):
            if (i%a) == 0:
                break
        else:
            color = randint(31, 37)
            print(f"\033[0;{color};40m {i}")
        i+=1


Job5()


