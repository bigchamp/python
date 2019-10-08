numb = 1 + 2 * 3 /4.0
print(numb)

reminder = 11 % 3
print(reminder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "Hello" + " World"
print(helloworld)

hellos = "hello" * 10
print(hellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
# all_numbers2 = odd_numbers - even_numbers
print(all_numbers)

array = [1,2,3]
new_array = array * 3
print(len(new_array))

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))