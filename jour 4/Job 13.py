#usage de fonction-in-built...
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
output = []
long = 0

for a in L:
    long+=1

for i in L:
    if i not in output:
        output.append(i)
print(output)
