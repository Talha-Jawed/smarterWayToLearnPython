# Touple immutable list/array
newToupleArray = (11, 22, 33, 44, 55)
print(newToupleArray)
print(newToupleArray[2])
print(newToupleArray.__len__())


name = str(input("Enter Your Name:"))  # Type casting you can use int str,float
print('Hello' + ' ' + name)

age = int(input("Enter Your age: ")) 
print(age + 5)



name = "TaLha"
print(name.upper())  # Change string to upper case
print(name.lower())  # Change string to lower case
print(name.title())  # change only the first character of word into uppercase
Data = {
    "name": "talha",
    "age": 22,
    5: 88
}  # just like object in javascript
print(Data)
# how to access that field of object/list also called dictionary in Python
print(Data["age"])
print(Data[5])  # a number can be a key
Data["city"] = "karachi"
print(Data)
del Data["age"]
print(Data)

for value in Data.values():  # to print the Value of keys
    print(value)


for valueOfKey in Data.keys():  # to print the Keys of the values
    print(valueOfKey)

for eachKey, eachValue in Data.items():  # To print both key and value we use this
    print("The key is " + str(eachKey) + " and the value is " + str(eachValue))


#  List of Dictionaries aka Array of object same sas Javascript object and array
arrayOfObjects = [
    {
        "name": "hello",
        "age": 13
    },
    {
        "name": "world",
        "age": 15
    }
]
print(arrayOfObjects)


# object containing array
arrayOfObjects.append({"numbers": [5555.54, 54, 53, 77]})
print(arrayOfObjects)


# You can also create object of objects

objectOfObjects = {
    0:{
        "name": "Talha Javed",
        "age": "22",
    },
    1:{
        "name": "Python",
        "age": "8",
    },
}
print(objectOfObjects)