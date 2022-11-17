# 1. Write a program to open the file created in Program 1 and compute the total marks and grade of all the students then display and save
# total marks and grade along with Name, RollNo, Marks, etc in the pre-existing file.


name=input("Enter your name : ")
rollno=input("Enter your roll no : ")
print("Enter the marks of 5 subjects : ")
phy=int(input("Physics : "))
chem=int(input("Chemistry : "))
math=int(input("Maths : "))
eng=int(input("English : "))
comp=int(input("Computer : "))
total=phy+chem+math+eng+comp
avg=total/5
if avg>=90:
    grade='A'
elif avg>=80:    
    grade='B'  
elif avg>=70:
    grade='C'
elif avg>=60:
    grade='D'
elif avg>=50:
    grade='E'
else:
    grade='F'

file=open("student_marks.txt","a")
file.write("*"*30)
file.write("\nName : "+name)
file.write("\nRoll no : "+rollno)
file.write("\nAverage : "+str(avg))
file.write("\nTotal marks : "+str(total))
file.write("\nGrade : "+grade)
file.write('\n')
file.write("*"*30)
file.close()

file=open("student_marks.txt","r")
print(file.read())
file.close()
