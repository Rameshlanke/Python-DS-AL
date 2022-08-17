class Student:
    def __init__(mysel, name, roll, marks):
        mysel.name = name
        mysel.roll = roll
        mysel.marks = marks

    def display(sel):
        print('Student Name: ',sel.name)
        print('Roll Number: ',sel.roll)
        print('Marks: ',sel.marks)
        print('\n')

S = Student('Ramesh', '18ME1037', 79.4)

S.display()
     
