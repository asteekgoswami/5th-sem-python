
num=int(input('Enter the decimal number :'))
x=num
lis=[]
while num!=0:
    r=num%2
    lis.append(r)
    num=num//2

lis.reverse()
print('Binary of the ',x," are :",end='')
bin=0
for i in lis:
    bin=bin*10+i
print(bin)

len=len(lis)
i=0
decimal_number=0
while i<len:
    rem=bin%10
    decimal_number=decimal_number+rem*(2**i)
    bin=bin//10
    i+=1
print('The decimal number are :',decimal_number)



