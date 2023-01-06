L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
def max_check(x):
  max_val = x[0]
  for check in x:
    if check > max_val:
      max_val = check
  return max_val

def min_check(x):
  min_val = x[0]
  for check in x:
    if check < min_val:
      min_val = check
  return min_val


print("Maximum", max_check(L))
print("Minimum", min_check(L))