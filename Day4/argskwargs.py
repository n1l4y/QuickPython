#args:

def addR(*argg):
    return sum(argg)

print(addR(10, 20, 30, 40, 50, 60, 70))

#kwargs keyword arguments

def func(**kwargs):
    if 'name' in kwargs:
        print("My name is {0}".format(kwargs['name']))
    if 'age' in kwargs:
        print("My age is {0}".format(kwargs['age']))
    else:
        print("No key found")

func(name='nilay', age='18')
