# 5. Write a program to create a file containing the record of employees with attributes Employee_Name, Emp_ID, Department, Basic_Pay, Total_Salary (Basic+DA+HRA+MA), where DA is 125% of Basic_Pay, HRA is 20% of Basic_Pay, MA is 10% of Basic_Pay.
# Compute the total salary and save the complete record of 10 employees in the file.

emp_name=input("Employee Name : ")
emp_id=input("Employee ID : ")
department=input("Department : ")
basic_pay=int(input("Basic pay : "))
da=1.25*basic_pay
hra=0.2*basic_pay
ma=0.1*basic_pay
total=basic_pay+da+hra+ma

file=open("employee.txt",'a')
file.write("\n")
file.write("*"*30)
file.write("\nEmployee Name : "+emp_name)
file.write("\nEmployee_id : "+emp_id)
file.write("\nDepartment : "+department)
file.write("\nBasic Pay : "+str(basic_pay))
file.write("\nTotal Salary : "+str(total))
file.write("\n")
file.write("*"*30)
file.close()

file=open("employee.txt","r")
print(file.read())
file.close()