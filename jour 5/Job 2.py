def draw_rectangle(num1, num2):
    i=0
    if num2 <=2:
        print("|", end="")
        print(num1 * "-", end="")
        print("|")
        print("|", end="")
        print(num1 * "-", end="")
        print("|")
    elif num2 >2:
        print("|", end="")
        print(num1 * "-", end="")
        print("|")

        while i < (num2 -2):
            print("|", end="")
            print(num1 * " ", end="")
            print("|")
            i+=1

        print("|", end="")
        print(num1 * "-", end="")
        print("|")
    print("")


draw_rectangle(10, 2)
draw_rectangle(11, 3)
draw_rectangle(12, 4)
