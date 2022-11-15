def triangle():
    base=float(input("Enter the base value : "))
    height=float(input("Enter the height value : "))
    area=(base*height)/2
    print("Area of triangle are : ","%.2f"%area)

def circle():
    rad=float(input("Enter the value of radius : "))
    area = 3.14*(rad**2)
    print("Area of circle are : ","%.2f"%area)

def rhombus():
    d1=float(input("Enter value of diagonal 1 : "))
    d2=float(input("Enter the valur of diagonal 2 : "))
    area=(d1*d2)/2
    print("Area of rhomus are : ","%.2f"%area)

def paralleogram():
    base=float(input("Enter the base value : "))
    height=float(input("Enter the height value : "))
    area=base*height
    print("Area of paralleogram are : ","%.2f"%area)

print("Press 1 to calculate the area of triangle ")
print("Press 2 to calculate the area of circle ")
print("Press 3 to calculate the area of Rhombus ")
print("Press 4 to calculate the area of parallelogram ")
n=int(input("Enter the choice : "))

match n:
    case 1:
        triangle()
    case 2:
        circle()
    case 3:
        rhombus()
    case 4:
        paralleogram()
    case _ :
        print("Enter the valid option ")
