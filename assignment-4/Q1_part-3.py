# Create a module of factorial, which can be called both in script and interpreter mode
import module
n=int(input("Enter the number to calculate the factorial : "))
x=module.factorial(n)
print("Factorial of ",n," is  : ",x)
