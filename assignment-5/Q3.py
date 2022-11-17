# 3. Write a program to create a file containing the information of patients of a hospital with attributes PatientName, PatientID, Age,
# Gender, Disease, Status(Cured or Not Cured) and Contact Number.

patient_name=input("Enter the patient name : ")
patient_id=input("Enter the patient id : ")
age=int(input("Enter the age of the patient : "))
gender=input("Enter the gender of the patient : ")
disease=input("Enter the disease of the patient : ")
status=input("Enter the status of the patient  (cured or not ) : ")
contact_number=input("Enter the contact number of the patient : ")


file=open("Hospital.txt","a")
file.write("*"*30)
file.write("\nPatient name : "+patient_name)
file.write("\nPatient id : "+patient_id)
file.write("\nAge : "+str(age))
file.write("\nGender :"+gender)
file.write("\nDisease : "+disease)
file.write("\nStatus : "+status)
file.write("\nContact number : "+contact_number)
file.write('\n')
file.write("*"*30)
file.close()

file=open("Hospital.txt","r")
print(file.read())
file.close()
