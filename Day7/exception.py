for i in range(3, -3, -1):
    try:
        print(1.0/i)

    except ZeroDivisionError as er:
        print("Zero Division Error: ", str(er.args[0]))
    
