a,b=0,1
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
        

n=int(input("Enter the range of fibonaccie series : "))
if n==1:
    print("The fibonaccie series are : ",a)
elif n<1:
    print("Please enter the valid number ")
else:
    print("The fibonaccie series are : ")
    for i in range(n):
        print(fib(i),end=" ")
    

