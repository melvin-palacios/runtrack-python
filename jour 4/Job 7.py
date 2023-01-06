L = [8, 24,48,2,16]
i = 0
for nombre in L:
    if (nombre % 3) == 0:
        print(f"{nombre} est un multiple de 3")
        i+=1
print(f"il y a {i} multiples de 3 dans cette liste")