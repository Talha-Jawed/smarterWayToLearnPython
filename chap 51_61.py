# chapter 51 - 61 and assignment no: 6

# How to use while loop python same as javscript
num = 0
newName, newPage = "hi", 22
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


givenName = Person("Talha Javed") 
givenName.nameofPerson()

# It also pass referanc just like javascript
newMember = givenName
print(newMember.name)
givenName.name = "Talha"
print(newMember.name)
a = 55
b = a
print(b)
a = 70
print(b)
print(a)


#  Assignment no: 6

class car(object):

    def __init__(self, color, vehicle, person):
        self.color = color
        self.vehicle = vehicle
        self.person = person

    def start(self):
        # %s is like `${this.value}` of javascript
        return "%s starting" % self.vehicle

    def brake(self):
        return "%s braking" % self.vehicle

    def drive(self):
        return "I am driving a %s %s! with %s person" % (self.color, self.vehicle, self.person)


civic = car("black", "civic", 3)
print(civic.brake())
print(civic.start())
print(civic.drive())
corolla = car("silver", "corolla", 3)
print(corolla.drive())
fortuner = car("white", "fortuner", 4)
print(fortuner.drive())
print(fortuner.brake())
