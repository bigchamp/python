x = 2

print(x == 2)
print(x == 3)
print(x < 2)

name = "Kairat"
age = 23

if name == "Kairat" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "Kairat" or name == "Rick":
    print("Your name is either John or Rick.")


# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list
name = "John"
listArr = ["John", "Rick"]

if name in listArr:
    print("Your name is either John or Rick.")