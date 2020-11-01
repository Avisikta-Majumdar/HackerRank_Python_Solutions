import itertools as it
iterr ,n = input().split(" ")
lst1= list(i for i in iterr)
str(lst1.sort())
result = []
for i in range(1,int(n)+1):
    x = list(m for m in it.combinations(lst1, i))
    result.append(x)
for m in range(len(result)):
    for j in result[m]:
        for k in j:
            print(k, end ="" )
        print()
