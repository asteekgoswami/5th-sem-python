# 2. Write a program to create a class Employee containing the data members emp_name, emp_ID, Dept, basic_pay,
#  HRA, DA, MA with member functions total_salary() [computes the total salary based on basic pay, HRA=20% of 
# basic_pay, DA=120% of basic_pay, and MA=5% of basic_pay] and emp_details, displays the complete details of
#  the employee


class Employee:
    def __init__(self) -> None:
        self.emp_name=''
        self.emp_id=''
        self.dept=''
        self.basic_pay=0
        self.total=0

    def getdata(self):
        self.emp_name=input("Employee Name : ")
        self.emp_id=input("Employee Id : ")
        self.dept=input("Department : ")
        self.basic_pay=int(input("Basic pay : "))

    def totalsalary(self):
        hra=0.2*self.basic_pay
        da=1.2*self.basic_pay
        ma=0.05*self.basic_pay
        self.total=self.basic_pay+hra+da+ma
        print("Total salary : ",self.total)
    
    def emp_details(self):
        self.totalsalary()
        print("-"*30)
        print("Employee Name : ",self.emp_name)
        print("Employee Id : ",self.emp_id)
        print("Department : ",self.dept)
        print("Basic Pay : ",self.basic_pay)
        print("Total Salary : ",self.total)
        print("-"*30)


ob=Employee()
ob.getdata()
ob.emp_details()