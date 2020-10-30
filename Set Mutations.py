# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input(""))
seta = set(map(int , input("").split(" ")))
j = int(input(""))
for i in range(j):
    ian = list(input().split())
    if ian[0]== "intersection_update":
        fi = set(int(x) for x in input('').split(" ")) 
        seta.intersection_update(fi)

    elif ian[0] == "symmetric_difference_update":
        fi = set(int(x) for x in input('').split(" "))
        seta.symmetric_difference_update(fi)

    elif ian[0] == "update":
        fi = set(int(x) for x in input('').split(" "))
        seta.update(fi)

    elif ian[0] == "difference_update":
        fi = set(int(x) for x in input('').split(" "))
        seta.difference_update(fi)
res = 0
for m in seta:
    res+=m
print(res)
