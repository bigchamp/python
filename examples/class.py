
class MyClass:
    variable = "Blah"

    def my_function(self):
        print("This is a message inside the class.")


my_own_class = MyClass()

x = my_own_class.variable
print(x)


my_own_class.my_function()

myobjectx = MyClass()
myobjecty = MyClass()

myobjectx.variable = "guzhigak"
myobjecty.variable = "asdasdasd"

print(myobjectx.variable)
print(myobjecty.variable)


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

# test code
car1 = Vehicle()
car1.name = "Toyota"
car1.color = 'black'
car1.kind = "car"
car1.value = 12000

car2 = Vehicle()

car1.name = "BMW"
car1.color = 'white'
car1.kind = "car"
car1.value = 35000

print(car1.description())
print(car2.description())