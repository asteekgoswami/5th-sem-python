# 2. Write a program to a file named Invoice of purchased items from a general store, which contains ItemNo, ItemName, Price, Quantity.
# Compute the total_bill then display and save the file along with preexisting data.

itemno=int(input("Enter the item number : "))
itemname=input("Enter the item name : ")
price=int(input("Enter the price of the item : "))
quantity=int(input("Enter the quantity of the item : "))
total_bill=price*quantity

file=open("Invoive.txt","a")
file.write("*"*30)
file.write("\nItem no : "+str(itemno))
file.write("\nItem name : "+itemname)
file.write("\nPrice : "+str(price))
file.write("\nQuantity : "+str(quantity))
file.write("\nTotal bill : "+str(total_bill))
file.write('\n')
file.write("*"*30)
file.close()

file=open("Invoive.txt","r")
print(file.read())
file.close()