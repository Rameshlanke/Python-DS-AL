class Student:
    '''This is Version 1.0'''
    def __init__(self):

        self.name = 'Ramesh'
        self.roll = '18ME1037'
        self.marks = '7.47'
    def __str__(self):
        return 'This is the Student Class'
    def display(self):
        print('StudentName: ',self.name)
        print('Roll Number: ',self.roll)
        print('Marks: ',self.marks)

#S - Student()
S = Student()
S1 = Student()
S2 = Student()
S3 = Student()
S.display()
S1.display()
S2.display()
S3.display()
print(S.name)
print(S.roll)
print(S.marks)
print(S.__doc__)
print(S)

def display(self):
    print('StudentName: ',S.name)
    print('Roll Number: ',S.roll)
    print('Marks: ',S.marks)
S.display()

