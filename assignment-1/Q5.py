from cmath import sqrt


print('Enter the quadratic equation in the form of Ax^2 +- Bx +- C=0')
a=int(input("Value of A :"))
b=int(input("Value of B :"))
c=int(input("Value of C :"))

x=-b+sqrt((b**2) - (4*a*c))/2*a

y=-b-sqrt((b**2) - (4*a*c))/2*a

print(x,y)


