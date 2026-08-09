for i in range(1,6):
  for j in range(1, i+1):
    print(j, end="")
  print()
#Repeated Number Triangle
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
#Inverted Number Triangle
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#Floyd's Triangle
num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
