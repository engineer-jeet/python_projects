class student:
    school_name = "SB Public School, Godda" # static variable

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno # instance variable

    def student_info(self): # instance Method
        x=10
        for i in range(x): # i is the local variable
            print(i, self.name)
    
    @classmethod # class method
    def m1(cls):
        print("school name: ", cls.school_name) # static variable)

    @staticmethod # static method
    def getSum(a,b): # local variables
        sum = a+b
        return sum
       

    

# methods - class methods - its a method where we use only static variable
# cls is the refernce variable pointing to the class object
# class test:
#     school_name = "SB Public School, Godda" # static variable

#     @classmethod # class method
#     def m1(cls):
#         print("school name: ", cls.school_name) # static variable)
#         print(id(cls))

#     # Static Method : general utility method
#     @staticmethod
#     def getSum(a,b):
#         return a+b 
    


# print(id(test)) 
# test.m1()
# print()





    


        