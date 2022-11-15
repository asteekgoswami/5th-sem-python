def simpleinterest(p,r,t):
    a=(p*r*t)/100
    print(a)
    return a

def compound(p,r,t):
    a=p*(1+(r/100))**t
    ci=a-p
    return ci

p=float(input("Enter the initial principle balanace : "))
r=float(input("Enter the annual interest rate : "))
t=float(input("Enter the time in years : "))
print("The simple interest are : ",simpleinterest(p,r,t))
print("The compound interest are : ","%.2f"%compound(p,r,t))