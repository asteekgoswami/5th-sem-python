# . Write a program to print prime numbers between certain interval.

a=int(input("Enter the number to start the range : "))
b=int(input("Enter the number to end the range : "))
print("The prime numbers between ",a," and ",b," are : ")
for i in range(a,b+1):
    n=0
    for j in range(2,i//2):
        if(i%j==0):
            n+=1
            break
    if n!=1:
        print(i,end=" ")