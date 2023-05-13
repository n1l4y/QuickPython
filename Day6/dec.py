#Decorators
'''
@decName
def func():
    print("statement")


EQUAL TO:

def func():
    print("statement")

func = decName(func)
    
'''
'''--------------------------------------'''
#Function in object

def welcome(a):
    print("Hello {0}, welcome to Python Bootcamp".format(a));

a = welcome
'''--------------------------------------'''
#Function in variable

def lowerCase(text):
    return text.lower()

def upperCase(text):
    return text.upper()

def a(welcome):
    message = welcome("Hello all, Welcome to Python Bootcamp")
    print(message)

a(lowerCase)
a(upperCase)
'''--------------------------------------'''
#Returning function from another function

def addMain(a):
    def addSub(b):
        print(a, b)
        return a+b
    return addSub

addition = addMain(100)
print(addition(75))

