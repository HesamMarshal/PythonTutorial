'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'global x'


def my_func():
    x = 'local x'
    print(x)


my_func()
print(x)
