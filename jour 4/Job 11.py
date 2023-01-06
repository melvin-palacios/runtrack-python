L = [7, 11, 42, 39, 2]

def add(string):
     i = 0
     while i < len(string):
         string[i] += 1
         i += 1
     return(string)

print(add(L))