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



# Assignment no: 2

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

