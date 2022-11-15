print('To genrate the prime number in certain range :')
start=int(input('Starting range :'))
end=int(input('End range :'))

for i in range(start,end+1):
    flag=0
    for j in range(2,i//2+1):
        if(i%j==0):
            flag=1
            break
    if flag!=1:
        print(i," is a prime number ")