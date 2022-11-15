def sumn(n):
    if n==1:
        return 1
    else:
        return n+sumn(n-1)

n=int(input("Enter the number to calculate the sum of n natural number : "))
print("Sum of ",n," natural numbers are : ",sumn(n))
