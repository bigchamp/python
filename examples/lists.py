mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

for x in mylist:
    print(x)

# Accessing an index which does not exist generates an exception
# print(mylist[10])

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
