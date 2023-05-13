def check(numbers):
    primeNumber = []
    for num in numbers:
        if num > 1:
            for i in range(2, int(num/2) + 1):
                if(num % i == 0):
                    print(num, "is not prime")
                    break
            else:
                print(num, "is prime")
                primeNumber.append(num)
    return primeNumber

print(check(list(x for x in range(21))))

#map function - used to pass individual iterable to function
#list(map(function_name, listname))


                
