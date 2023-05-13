class Student:
    Total = 500
    def __init__(self, marks):
        self.marks = marks
        print("Initialized...")

    def findLoss(self):
        return self.Total - self.marks

    def findPercentage(self):
        return self.marks/self.Total*100

a = Student(450)
print("Loss is", a.findLoss())
print("Percentage is", a.findPercentage())

class Student2:
    def __init__(self, name, marks, gender):
        self.name = name
        self.marks = marks
        self.gender = gender
        print("Initialized")

    def __len__(self):
        return self.marks

    def __str__(self):
        return "Name: %s | Marks: %s | Gender: %s" %(self.name, self.marks, self.gender)

    def __del__(self):
        print("Student Database is Deleted")

a = Student2('champ', 450, 'male')
print(a)
print('Marks: ', len(a))
