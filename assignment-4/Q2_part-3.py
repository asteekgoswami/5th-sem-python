#  Create a module of fibonacci series, which can be called both in script and interpreter mode.
import module
n=int(input("Enter the number of terms : "))
# for it in module.fibonacci(n):
#     print(it,end=" ")
for i in range(n):
    print(module.fibonaccii(i),end=" ")