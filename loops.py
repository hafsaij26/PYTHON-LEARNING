# if 
a = 10
b = 5

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b) 

#if else
marks = int(input("enter your marks: "))
if marks > 50 :
  print("You are pass")
else: 
  print("fail")

  #if-elif-if
age = int(input("enter your age : "))
if age<=17 :
  print("you are not wiligible for vote")
elif 50> age >=18:
  print("you are ARE eiligible for vote")
elif age>=50:
  print("you are too old for vote")
else:
  print("invalid")

### for loop
for i in range(2) : print ("HELLO WORLD")
for i in range(1,4) : print (i)
#start,stop,step
for i in range(2, 15, 4) : print(i)
#backword
for i in range(10, 0, -1) : print(i , end=" " )
print()
#in string
for ch in "Hafsa" : print(ch , end="")
#loop list
for item in (1,2,3):
    print(item)


name = "Python"

for i in range(len(name)):
    print(name[i])

st_name = "HAFSAIJAZ"
for i in range (len(st_name)):
    print (st_name[i])

#loop through dictionary
student = {"name : ": "Hafsa", "age": 21}

for key, value in student.items():
    print(key, value)
for key in student():
    print(key)

for value in student.items():
  print(value)

#while loop
count=1
while(count <= 17):
  print(count)
  count+= 1

print("hello")
#false loop
while False:
    print("Hello")

print("Finished")

i = 1

while i <= 20:
    print(i)
    i *= 2
#centimental controll loop
number = 0

while number != -1:
    number = int(input("Enter number (-1 to stop): "))
#counter control loop
count = 1


while count <= 5:
    print(count)
    count += 1

i = 1

while True:
    print(i)

    if i == 5:
        break

    i += 1


i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue

    print(i)