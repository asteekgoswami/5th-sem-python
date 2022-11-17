# 4. Write a program to create a file exhibiting the data of a bank account with details, CustomerName, AccountNo, AccountType, Balance, and Contact Number.

customer_name=input("Customer Name : ")
account_number=input("Account Number : ")
account_type=input("Account Type : ")
balance=input("Balance : ")
contact_number=input("Contact Number : ")

file=open("bank.txt",'a')
file.write('\n')
file.write("*"*30)
file.write("\nCustomer Name : "+customer_name)
file.write("\nAccount NUmber :"+account_number)
file.write("\nAccount Type : "+account_type)
file.write("\nBalance : "+balance)
file.write("\nContact Number : "+contact_number)
file.write('\n')
file.write("*"*30)
file.close()

file=open("bank.txt",'r')
print(file.read())
file.close()

