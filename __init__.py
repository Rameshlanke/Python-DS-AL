
class Student:
    def __init__(self):
        self.name='Ramesh'
        self.roll='18ME1037'
        self.marks=78.7
        print("In Constructor")
    def display(self):
        print(self.name, self.roll, self.marks)

S = Student()
S.__init__()
