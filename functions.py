#first function
def greet():
    print("Hello! Welcome to the program.")

greet()
greet()
greet()
#parameter
def greet(name):
    print("Hello", name)

greet("hafsa")

#Function Returning a Value
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)
print("The area of the rectangle is:", result)

#print and return
def add(a,b):
  return a+b
x=add(10,10)

def sub(a,b):
  print(a-b)

print(x)
sub(10,5)

#variable
def demo():
  x=12
  return x

demo()
#check even and odd
def check(a):
  if(a%2==0):
    print("even")
  elif(a%2==1):
    print("odd")

check(9)

def sq(num):
  return num*num
sq(3)

def add(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))

def hello():
    for i in range(5):
        print("Hello")

hello()

def print_numbers():
    for i in range(1, 11):
        print(i)
print_numbers()

for row in range(5):
    for col in range(5):
        print("*", end="")
    print()

for row in range(1, 6):
    for col in range(1, row + 1):
        print("*", end=" ")
    print()
for row in range(5, 0, -1):
    for col in range(1, row + 1):
        print("*", end=" ")
    print()
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()