
class Student:
    '''This is Version 1.0'''

    def __init__(self, name, roll, marks):

        self.name = name
        self.roll = roll
        self.marks = marks
    def __str__(self):
        return 'This is the Student Class'

    def display(self):
        print('Student Name: ',self.name)
        print('Roll Number: ',self.roll)
        print('Marks: ',self.marks)
        print('\n')

S = [Student('Ramesh', '18ME1037', 79.4),
     Student('Keerthi', '18CE1024', 87.9),
     Student('Satish', '15TD1017', 78.5)]

for i in S:
    i.display()
