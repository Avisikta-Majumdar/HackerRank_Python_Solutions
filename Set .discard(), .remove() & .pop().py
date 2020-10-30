n = int(input())
s = set(map(int, input().split(" ")))
m = int(input())
for i in range(0,m):
    x=list(input().split(" "))
    if x[0]=="pop":
        s.pop()
    elif x[0]=="remove":
        j = int(x[1])
        s.remove(j)
    elif x[0]=="discard":
        j = int(x[1])
        s.discard(j)
print(sum(s))
