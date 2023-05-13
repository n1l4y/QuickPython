while True:
    try:
        a = int(input("Enter a number a: "))
        b = int(input("Enter a number b: "))

    except:
        print("Not valid")
        continue

    else:
        print("Valid number")
        break

    finally:
        print("code end")

    
