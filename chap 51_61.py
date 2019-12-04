# chapter 51 - 61

# How to use while loop python same as javscript
num = 0
newName,newPage = "hi",22
print(newPage)
print(newName) 
while num < 5:
    print("hello world")
    num += 1


class Person:
    def __init__(self, fullName):  # this is class constructor
        self.name = fullName  # self is like "this" of javascript
    def nameofPerson(self):
        print(self.name)


Talha = Person("Talha Javed")
Talha.nameofPerson()

# It also pass referanc just like javascript
newMember = Talha
print(newMember.name)
Talha.name = "Talha"
print(newMember.name)
a = 55
b = a
print(b)
a = 70
print(b)
print(a)
