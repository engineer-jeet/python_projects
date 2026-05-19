# ways of adding / accessing instance variables
class test:

    def __init__(self):
        self.a = 10
        self.b = 20
    
    def m1(self):
        self.c = 30

t = test()
t.m1()
t.d = 40
t1 = test()

print(t.__dict__)
print(t1.__dict__)
#print(t.__dict__.items())
# notice : the number of instance variable is changing from object to object








    


