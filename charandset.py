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
#value
for value in student.values():
    print(value)
#both
for key, value in student.items():
    print(key,":", value)

#set
a={1,2,3,4,5}
print(a)
b={4,5,6,7,8}
print(b)
#union
print(a|b)
print(a.union(b))
#intersection
print(a&b)
print(a.intersection(b))
