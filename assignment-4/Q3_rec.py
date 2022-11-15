# . Write a program to print tower of Hanoi using recursion.

def toh(n,frm,to,aux):
    if n==1:
        print("Move disk from ",frm," to ",to)
        return
    toh(n-1,frm,aux,to)
    print("Move disk from ",frm," to ",to)
    toh(n-1,aux,to,frm)

n=int(input("enter the no. of disk : "))
t1=input("enter the initial tower : ")
t2=input("enter the destination tower : ")
t3=input("enter the auxilary tower : ")
toh(n,t1,t2,t3)