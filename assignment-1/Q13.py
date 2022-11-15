num=int(input('Enter a number to determine an Armstrong number or not :'))
x=num
y=0
l=len(str(num))
while num!=0:
    r=num%10
    y=y + r**l
    num=num//10

if x==y:
    print(x,' is a Armstrong number')
else:
    print(x,' is not a Armstrong number')

