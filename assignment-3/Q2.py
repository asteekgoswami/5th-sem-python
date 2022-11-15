def cal(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
    elif op=="//":
        return a//b
    else:
        print("Enter the valid operand ")
a=float(input("Enter the 1st number : "))
b=float(input("Enter the 2nd number : "))
op=input("Enter the operand : ")

print("Result : ",cal(a,b,op))