#map function - used to pass individual iterable to function
#list(map(function_name, listname))

def evenFn(num):
    return num % 2 == 0

a = [0,1,2,3,4,5,6,7,8,9]
print(list(map(evenFn, a)))
print(list(filter(evenFn, a)))
