# Write a program to compute mean, variance, and, standard deviation
def mean(lis):
    return sum(lis)/len(lis)
def variance(lis):
    m=mean(lis)
    d=0
    for i in lis:
        d=d+(i-m)**2
    return d/len(lis)
def standard_deviation(lis):
    v=variance(lis)
    s=v**0.5
    return s
lis=list(int (i) for i in input("Enter the list seperated by space : ").split(" "))
print("Mean : ",mean(lis))
print("Variance : ",variance(lis))
print("Standard deviation are : ",standard_deviation(lis))
# 4, 8, 6, 5, 3, 2, 8, 9, 2, 5