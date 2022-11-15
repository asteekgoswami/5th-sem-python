lis=[int(i) for i in input('Enter the elements of list seperated by space :').split(' ') if ord(i)>=49 and ord(i)<=57]
#way-1
summ=0
for i in lis:
    summ=summ+i

print('sum by for loop :',summ)
len=len(lis)
print('Average of list are :',summ/len)

#way-2
# print(sum(lis))
