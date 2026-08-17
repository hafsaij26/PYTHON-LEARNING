class student:
    
    def __init__(self, n, i):
        self.n=n
        self.i=i
    def name(self):
        return self.n
    def id(self):   
        return self.i

s1= student("HAFSA", 127)
print(s1.name())
print(s1.id())
