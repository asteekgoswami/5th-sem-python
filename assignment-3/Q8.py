# Write a program to compute factorial of a number
def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)

n=int(input("Enter the number to calulate the factorial : "))
print("The factorial of ",n," are : ",fac(n))