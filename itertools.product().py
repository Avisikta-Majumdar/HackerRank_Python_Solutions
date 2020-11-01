import itertools as it
a = list(map(int , input("").split(' ')))
b = list(map(int , input("").split(' ')))
lst = list(x for x in it.product(a,b))
for i in lst:
    print(i, end = ' ' )
