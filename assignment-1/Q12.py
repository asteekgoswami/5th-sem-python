num = int(input('Enter a number to check that it is prime or not :'))
for i in range(2, num//2):
        if(num % i == 0):
            print(num, ' is not a prime number ')
            break
        i+=1
else:
    print(num,' is a prime number ')
