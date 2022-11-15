# Write a program to compute sum of A. P. series

lis=list(int(i) for i in input("Enter the series numbers seperated by space : ").split(" "))
n=len(lis)
a1=lis[0]
an=lis[-1]
sum=n/2*(a1+an)
print("Sum of A.P series are : ",sum)