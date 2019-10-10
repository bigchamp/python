def my_function():
    print('my first function')


my_function()

def my_function_with_args(name, surname):
    print("Hello, %s %s, Happy birthday to you" % (name, surname))


my_function_with_args('Kamil', 'Kowalski')


def func_addition(a, b):
    total = a + b
    print("%d + %d is equal to %d" % (a, b, total))


func_addition(4, 5)
