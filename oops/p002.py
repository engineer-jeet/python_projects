class student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    
    def talk(self):
        print('Hello, I am: ', self.name)
        print('My Rollno is: ', self.rollno)
        print('My mark is: ', self.marks)

s = student('Jeet', 101, 90)
s1 = student('Sonal', 201, 95)


s1.talk()

        