myInt = 7
print(myInt)

myInt = int(7)
print(myInt)

myFloat = 7.0
print(myFloat)

myFloat = float(9)
print(myFloat)

myString = 'hello'
print(myString)

myString = "hello"
print(myString)

myString = "Don't worry with apostroph"
print(myString)

one = 1
two = 2
result = one + two
print(result)

a, b = 4, 6
print(a, b)

one = 1
two = 2
hello = "hello"

# Mixing operators between numbers and strings is not supported
# print(one + two + hello)

# change this code
mystring = "hello"
myfloat = float(10)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)