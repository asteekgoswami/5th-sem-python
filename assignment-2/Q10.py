print('All the possible combinations of 4, 5, and 6 :')
# lis=[4,5,6]
# for i in lis:
#     for j in lis:
#         for k in lis:
#             if i!=j and j!=k and k!=i:
#                 print(i," ",j," ",k)

from itertools import permutations
com=permutations([4,5,6],3)
for i in com:
    print(i)