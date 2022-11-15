# . Write a program to shuffle a deck of cards

import itertools, random


dec=list(itertools.product( range(1,11),['Spade','Heart','Diamond','Club']))

random.shuffle(dec)
print("The deck are shuffled ! ")
num=int(input("Enter the number of cards you want to drawn : "))
for i in range(0,num):
    print(dec[i][0] ," of ",dec[i][1])
