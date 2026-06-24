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