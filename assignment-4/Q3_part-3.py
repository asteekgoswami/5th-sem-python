#  Write a program to evaluate the following expressions (see attachment) using functions/modules
import module

print('To eval this exprrssion :')
print('x-x^3/3! + x^5/5! - x^7/7! + .... x^n/n!')
print('x-x^2/2! + x^3/3! - x^4/4! + .... x^n/n!')
num=int(input("Enter the value n : "))
x=int(input("Enter the value of x :"))


print(module.normal_eval(1,x,num,0,1))
print(module.odd_eval(1,x,num,0,1))