L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
lenght = len(L)
i = 0
v = 0
while i < lenght:
    if (L[i] % 2 == 0):
        v = v + L[i]
    i = i + 1

print(v)