def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    


def fibonaccii(n):
    if n<=1:
        return n
    else:
        return fibonaccii(n-1)+fibonaccii(n-2)

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
        