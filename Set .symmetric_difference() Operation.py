a0 = int(input(""))
s = set(filter(int , input("").split(' ')))
a1 = int(input(""))
Final_Set = set(filter(int , input("").split(' ')))
SetA = s.symmetric_difference(Final_Set)
output = 0
for i in SetA:
    output+=1
print(output)
