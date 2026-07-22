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
  

while True:
    print(" Student Menu ")
    print("1. Enter Student Information")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_info()

    elif choice == "2":
        print("Thank you! Program Closed.")
        break

    else:
        print("Invalid Choice! Please try again.")