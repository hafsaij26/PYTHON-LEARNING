# started functions
print ("hello world")
#VARIABLES
name = "HAFSA"
age = 21
rollno = 008
is_student = True
print (name)
print (age)
print (is_student)
# end functions
# DATATYPES
print (type(name))
print (type(age))
print (type(rollno))
print (type(is_student))
#input function
name = input("what is your name? ")
print (name)
# Calculation
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print ("SUM IS ", num1 + num2)
print("Length of sum is " , len(str(num1 + num2)))
mess = f'welcome to my {num1} world to {num2}';
print(mess)
name = "mohsin"
age = 12
gender ="male"
mess2 = 'your name is {} and your age is {} and your gender is {}'.format(name, age, gender)
print(mess2)