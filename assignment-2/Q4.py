from math import prod


print('Enter the 10 elements :')
# take input in different line
lis=[int(input()) for i in range(10)] 
# # take input in single line
# lis=list(map(int,input().split(' '))) 
sum=0
product=1
for i in lis:
    if i%2==0:
        sum=sum+i
    else:
        product=product*i


print('Sum os even numbers are :',sum)
print('Product of odd numbers are :',product)