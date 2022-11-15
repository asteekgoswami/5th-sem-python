
lis=[int(i) for i in input('Enter the list of numbers :').split(' ') if ord(i)>=49 and ord(i)<=57 ]
max=0
min=lis[0]
for i in lis:
    if i>max:
        max=i
    elif i<min:
        min=i
    
print('Biggest number are :',max)
print('Smallest number are :',min)
    


