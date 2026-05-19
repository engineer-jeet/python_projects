class student:
    '''class developed by Jeet'''
    def __init__(self):
        self.name = "Jeet"
        self.rollno = 101
        self.marks = 90

    def talk(self):
        print('Hello, I am: ', self.name)
        print('My Rollno is: ', self.rollno)
        print('My mark is: ', self.marks)


s = student()
print(s.name, s.rollno, s.marks)
print()
s.talk()