f = open("welcome.txt", "r")
print(f.read())
f.close()
f = open("welcome.txt", "r")
for x in f:
    print(x)
