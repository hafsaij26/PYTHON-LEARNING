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