# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools as it
itere , n =input("").split(" ")
lst1 =(list(i for i in itere))
str(lst1.sort())
n=int(n)
lst = list( x for x in it.permutations(lst1 , n))
for i in lst:
    m = ""
    for j in i:
        m+=j
    print(m)

