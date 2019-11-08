# chapter 1-11 and assignment no. 1 

import sys
import math
import datetime

# print
msg = "My Name is Talha"
print(msg)

# Numbers
number = 123456
number += 1
print(number)
concatination = "19" + "97"
print(concatination)

# Bodmas rules
num = 4 * 8 / 2 + 10  # Division single / show result in point(.) & double not show point(.)
print(num)


# Concatenating strings
firstName = "Talha"
lastName = "Javed"
fullName = firstName + ' ' + lastName
print(fullName)

greeting = "Hello"
space = " "
address = "World"
separators = "!"
whole_greeting = greeting + space + address + separators
print(whole_greeting)

# if else statment
if ('hello' == 'hello'):
    print('condition true')
else:
    print('condition false')

if (2 > 2):
    print("Talha")
elif ('python' == 'javaScript'):
    print("elif ")
else:
    print("else")



# assignment no. 1

pythonVarsion = "Python version: " + sys.version  
print (pythonVarsion)

print ("Version information: ")
print (sys.version_info)


now = datetime.datetime.now()
print(now)


r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(math.pi * r**2))
