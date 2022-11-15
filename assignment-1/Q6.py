n=int(input('Enter the range '))

for i in range(n+1):
    if i%3==0 or  i%6==0 or i%9==0:
        continue
    print(i)

