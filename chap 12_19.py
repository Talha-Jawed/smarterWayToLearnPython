# Chapter 12-19 & assignment 2

#  And and or operator
if 4 > 2 and 5 > 4:
    print("and contdition true")

if 'hello' == 'hello' and 'world' == 'abc':
    print("and contdition false")

if 9 < 7 or "talha" == "talha":
    print("or condition true")

if 9 < 7 or "hello" == "world":
    print("or condition false")


# if statment nested
if 1 == 1:
    if 2 != 2:
        print("nested if")
    elif 'abc' == 'abc':
        print('nested elif')
    else:
        print("nested else")
else:
    print('else nested')


# single line comment using "#"
# multi line comment using " ''' "

'''
my name
is talha
multiple line comment
'''


# List in python aka array
numbers = [6, 5, 4, 3, 2, 1]
print(numbers)
print(numbers[4])
print(numbers.__len__())

# # using append push in js

numbers.append(45)
print(numbers)
numbers.pop()
print(numbers)
numbers.insert(3, 99)
print(numbers)

# slice in python

num = [11, 12, 13, 14, 15, 16]
newArray = num[2:5] # print index 2 to 5
print(newArray)
del num[0]
print(num)
num.remove(12) # delete using value
print(num.pop()) # print last value



# Assignment no: 2 & 3


# Marksheet

print("Marks of Five Subjects")
sub1=int(input("Enter marks of English: "))
sub2=int(input("Enter marks of Math: "))
sub3=int(input("Enter marks of Science: "))
sub4=int(input("Enter marks of Urdu: "))
sub5=int(input("Enter marks of Islamiat: "))
tmarks=sub1 + sub2 + sub3 + sub4 + sub4
print("Total marks" , tmarks , 'out of 500')
percentage= tmarks / 500 * 100
print(percentage , '%')
if(percentage >= 90 and percentage <= 100):
    print("Grade: A+")
elif(percentage >= 80 and percentage < 90):
    print("Grade: A")
elif(percentage >= 70 and percentage < 80):
    print("Grade: B")
elif(percentage >= 60 and percentage < 70):
    print("Grade: C")
elif(percentage >= 50 and percentage < 60):
    print("Grade: D")
else:
    print("Fail")



# calculator

val1 = int(input('Enter First Value: '))
operator = (input('Enter Operator: '))
val2 = int(input('Enter Second Value: '))

if operator == '+':
    print(val1 + val2 ,'answer')
elif operator == '-':
    print(val1 - val2 ,'answer')
elif operator == '*':
    print(val1 * val2 ,'answer')
elif operator == '/':
    print(val1 / val2 ,'answer')
else:
    print('Please Enter Valid Operator')



#duplicate values from list

arr = [ 3, 54, 59, 3, 89, 30, 12, 6, 54, 33, 30, 10]
dupItems = []
uniqItems = {}
for i in arr:
   if i not in uniqItems:
        uniqItems[i] = 1
   else:
        if uniqItems[i] == 1:
            dupItems.append(i)
        uniqItems[i] += 1
print(dupItems)