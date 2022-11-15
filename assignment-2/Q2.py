from cmath import *

# print('Enter the edge of cube to find the volume of cube :')
# edge=float(input('Edge :'))
# volofcube=edge**3
# print('Volume of cube are','%.2f'%volofcube)

# print('Enter the value of radius and height to find the volume of cylinder :')
# rad=float(input("Radius :"))
# height=float(input("Height :"))
# volofcyl=pi*rad**2*height
# print('Volume of cylinder :','%.2f'%volofcyl)

print("Enter the value of radius and height to find the volume of cone :")
radius=float(input('Radius :'))
height=float(input("Height :"))
volofcone=pi*radius**2*(height/3)
print('Volume of cone :','%.2f'%volofcone)