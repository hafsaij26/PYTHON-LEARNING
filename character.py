for i in range(65,70):
    print(chr(i))
 for i in range(65, 70):
...     for j in range(65, i+1):
...         print(chr(i), end ="")
...     print()
for i in range(65 , 70):
     for j in range(65, i+1):
         print(chr(j), end="")
     print()
n=65
for i in range(65, 91):
    for j in range(65, i+1):
        print(chr(n), end="")
        n=n+1
    print()

#dictionaries
student={"name": "Hafsa", "age": 21, "city": "Karachi"}
print(student())
print(student.get("name"))

#add value
student["roll no."]=123
print(student)
#remove value
student .pop("age")
print(student)
#key
for key in student:
    print(key)
