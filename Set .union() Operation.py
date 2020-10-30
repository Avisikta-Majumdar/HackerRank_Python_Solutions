n1 = int(input(""))
ls1=set(map(int , input("").split(" ")))
n2 = int(input(""))
ls2=set(map(int , input("").split(" ")))
ma = set(ls1.union(ls2))
output =0
for i in ma:
    output+=1

output = str(output)
print(output)
