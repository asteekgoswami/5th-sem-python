print('Enter the two number to find the HCf :')
a=int(input('1st number :'))
b=int(input('2nd number :'))

for i in range(1,min(a,b)):
    if a%i==0 and b%i==0:
        x=i

print('HCF of ',a,'and ',b,' are :',x)