#little projects
def student_info():
  name = input("enter your name: ")
  num= int( input("enter your number : "))
  print("name: ",name)
  print("number: ",num)

  if(num>=60):
    print("you are pass")
  elif(num<60):
    print("you are fail")
  else:
    print("invalid number")
  

student_info()