num=int(input('Enter the number to find the factorial of that number :'))
x=num
product=1
if num<0:
    print('Sorry factorial of negative number does not exist ')
elif num==0:
    print('Factorial of 0 is  : 1')
else:
    while num!=0:
        product=num*product
        num-=1
print("Factorial of the ",x, " are :",product)
