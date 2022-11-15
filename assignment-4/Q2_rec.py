# . Write a program to compute GCD using recursion

def gcd(a,b):
    if b==0:
        return a
    if a==0:
        return b
    else:
        return gcd(b,a%b)       

a=int(input("enter the first number : "))
b=int(input("enter the second number : "))
print("GCD of ",a," and ",b," is ",gcd(a,b))
