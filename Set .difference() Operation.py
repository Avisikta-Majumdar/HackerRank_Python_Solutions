m = int(input(""))
ma = set(map(int , input("").split(" ")))
m1 = int(input(""))
ma1 = set(map(int , input("").split(" ")))
Final_Set = ma.difference(ma1)
output = 0
for i in Final_Set:
    output+=1
print(output)
