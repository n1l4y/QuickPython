class Elon:
    def __init__(self):
        print("Profile created")

    def name(self):
        print("Elon Musk")

    def age(self):
        print(40)

class SpaceX(Elon):
    def __init__(self):
        Elon.__init__(self)
        print("Compay Profile created")

    def name(self):
        print("SpaceX")

    def type(self):
        print("Private Space travel")

a = SpaceX()
a.name()
