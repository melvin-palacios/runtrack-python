def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            if a == b or b == c or a == c:
                print("c'est un triangle isocèle rectangle")
            else:
                print("c'est un triangle rectangle")
        elif a == b and b == c:
            print("c'est un triangle équilateral")
        elif a == b or b == c or a == c:
            print("c'est un triangle isocèle")
        else:
            print("c'est un triangle quelconque")
    else:
        print("erreur")


triangle(4, 3, 5)
triangle(10, 10, 10)
triangle(10, 10, 12)
triangle(11, 10, 12)
triangle(5, 5, 10)
