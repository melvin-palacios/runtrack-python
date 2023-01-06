L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
lenght = 0
for a in L:
    lenght+=1
i = 0
while i < lenght - 1:
    if L[i] > L[i + 1]:
        L[i], L[i + 1] = L[i + 1], L[i]
        i = 0
    else:
        i+=1

print(L)