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

class car:
    def _init_(self, name, brand, number):
        self.name=name
        self.brand=brand
        self.number=number
    def display(self):
        return self.name, self.brand, self.number
car1= car("Civic", "Honda", 1234)
print(car1.display())
# encapsulation
class Bankaccount:
    def __init__(self, account, balance):
        self.__account=account
        self.__balance=balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
account1= Bankaccount("123456", 1000)
account1.deposit(500)
print(account1.get_balance())
account1.withdraw(200)
print(account1.get_balance())
