def calcule(num1, operator, num2):
    if operator == "/":
        print(num1 / num2)
    elif operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "%":
        print(num1 % num2)
    else:
        print("Veuillez réessayer")
calcule(10, "/", 5)
calcule(10, "+", 10)
calcule(10, "-", 2)