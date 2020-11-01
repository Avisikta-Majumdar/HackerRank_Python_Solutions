from itertools import combinations_with_replacement
lst , n = input("").split(" ")
n= int(n)
lst1 = list(x for x in lst)
lst1.sort()
lst = ''
for j in lst1:
    lst+=j
final = list(m for m in combinations_with_replacement(lst,n))
for x in final:
    s=''
    for i in x:
        s+=i
    print(s)
