n=int(input("Enter the no. to check weather it is palindrome or not :"))
x=n
y=0
while n>0:
    z=n%10
    y=y*10+z
    n=n//10
if y==x:
    print(x,' is a palindrome number')
else:
    print(x,' is not a palindrome number')
