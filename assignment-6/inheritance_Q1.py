# 1. Write a program to input students details and marks then compute total marks and percentage and 
# display the entire result using the single, multiple, and multilevel inheritance.

# class single_stundent:
#     def __init__(self) -> None:
#         self.name=''
#         self.age=''
#         self.roll_no=0
#         self.eng=0
#         self.maths=0
#         self.phy=0
#         self.chem=0
#         self.cs=0
#     def input_details(self):
#         self.name=input("Enter your name : ")
#         self.roll_no=int(input("Enter your roll no. : "))
#         self.age=input("Enter your age : ")

#     def input_marks(self):
#         print("Enter the marks ")
#         self.eng=int(input("English : "))
#         self.maths=int(input("Maths : "))
#         self.phy=int(input("Physics : "))
#         self.chem=int(input("Chemistry : "))
#         self.cs=int(input("Computer science : "))

#     def compute(self):
#         total=self.eng+self.maths+self.phy+self.chem+self.cs
#         print("*"*30)
#         print("Total marks out of 500 is : ",total)
#         print("Percentage : ",total/5)
#         print("*"*30)


# single=single_stundent()
# single.input_details()
# single.input_marks()
# single.compute()


# multilevel
# class student:
#     def __init__(self) -> None:
#         self.name=''
#         self.age=''
#         self.roll_no=0
#         self.eng=0
#         self.maths=0
#         self.phy=0
#         self.chem=0
#         self.cs=0
    
#     def input_details(self):
#         self.name=input("Enter your name : ")
#         self.roll_no=int(input("Enter your roll no. : "))
#         self.age=input("Enter your age : ")

# class student_2(student):
#     def input_marks(self):
#         print("Enter the marks ")
#         self.eng=int(input("English : "))
#         self.maths=int(input("Maths : "))
#         self.phy=int(input("Physics : "))
#         self.chem=int(input("Chemistry : "))
#         self.cs=int(input("Computer science : "))

# class student_3(student_2):
#     def compute(self):
#         total=self.eng+self.maths+self.phy+self.chem+self.cs
#         print("*"*30)
#         print("Total marks out of 500 is : ",total)
#         print("Percentage : ",total/5)
#         print("*"*30)


# multi_level_obj=student_3()
# multi_level_obj.input_details()
# multi_level_obj.input_marks()
# multi_level_obj.compute


# multiple
class student:
    def __init__(self) -> None:
        self.name=''
        self.age=''
        self.roll_no=0

    def input_details(self):
        self.name=input("Enter your name : ")
        self.roll_no=int(input("Enter your roll no. : "))
        self.age=input("Enter your age : ")

class marks:
    def __init__(self) -> None:
        self.eng=0
        self.maths=0
        self.phy=0
        self.chem=0
        self.cs=0
    
    def input_marks(self):
        print("Enter the marks ")
        self.eng=int(input("English : "))
        self.maths=int(input("Maths : "))
        self.phy=int(input("Physics : "))
        self.chem=int(input("Chemistry : "))
        self.cs=int(input("Computer science : "))

class compute(student,marks):
    def compute(self):
        total=self.eng+self.maths+self.phy+self.chem+self.cs
        print("*"*30)
        print("Total marks out of 500 is : ",total)
        print("Percentage : ",total/5)
        print("*"*30)

obj=compute()
obj.input_details()
obj.input_marks()
obj.compute()

    
        

    
