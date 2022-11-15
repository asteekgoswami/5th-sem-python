print('Enter the three sides of triangle :')

a=int(input('1st side :'))
b=int(input('2nd side :'))
c=int(input('3rd side :'))

if a==b or a==c or b==c:
    print('Triangle is isosceles')
else:
    print('Triangle is not isosceles')