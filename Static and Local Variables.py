class Student:
    college = 'PEC' #Static Variable
    def __init__(mysel, name, roll, marks):
        mysel.name = name
        mysel.roll = roll
        mysel.marks = marks
        Student.college = 'PEC'

    def display(sel):
        print("Student Name: ",sel.name)
        print("Roll Number: ",sel.roll)
        print("Marks: ",sel.marks)
        print("College Name:",Student.college) #Static Varaible
        #when ever we are calling static varriables these are called by class name
        print()

Student.college = 'PEC'
S1 = Student('Ramesh', '18ME1037', 79.4)
S2 = Student('Keerthi', '18CE1024', 87.4)

S1.display()
S2.display()
     
