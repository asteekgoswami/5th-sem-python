# 1. Write a program to evaluate the following expressions (see attachment)

def fib(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p

def normal_eval(s,x,n,ans,op):
    ans=0
    for i in range(1,n+1):
        if op==1:
            t=x**i/fib(i)
            ans=ans+t
            op=0
        else:
            t=x**i/fib(i)
            ans=ans-t
            op=1
    return ans

def odd_eval(s,x,n,ans,op):
    ans=0
    for i in range(1,n+1,2):
        if op==1:
            t=x**i/fib(i)
            ans=ans+t
            op=0
        else:
            t=x**i/fib(i)
            ans=ans-t
            op=1
    return ans
        
        



print('To eval this exprrssion :')
print('x-x^3/3! + x^5/5! - x^7/7! + .... x^n/n!')
print('x-x^2/2! + x^3/3! - x^4/4! + .... x^n/n!')
num=int(input("Enter the value n : "))
x=int(input("Enter the value of x :"))


print(normal_eval(1,x,num,0,1))
print(odd_eval(1,x,num,))

