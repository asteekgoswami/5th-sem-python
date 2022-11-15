# Write a program to convert decimal number to equivalent binary, octal, and hexadecimal numbers.

def binary(num):
    b=''
    while num:
        r=num%2
        b+=str(r)
        num=num// 2
    return b[::-1]


def octal(num):
    x=''
    while num:
        r=num%8
        x=x+str(r)
        num=num//8
    return x[::-1]


def hexdec(num):
    x=''
    while num:
        r=num%16
        if r>10:
            x+=chr(r+55)
        else:
            x=x+str(r)
        num=num//16
    return x[::-1]



num=int(input("Enter any decimal number : "))
print("The binary of the ",num," are : ",binary(num))
print("The octal of the ",num," are : ",octal(num))
print("The hexadecimal of the ",num," are : ",hexdec(num))



