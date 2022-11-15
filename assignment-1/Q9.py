n=int(input('Enter the range of fibonacci serie :'))

x=0
y=1
z=0

if n==1:
    print(x)

elif n==2:
    print(x," ",y)

else:
    print(x," ",y,end='')
    for i in range(2,n):
        z=x+y
        print(' ',z,end='')
        x=y
        y=z