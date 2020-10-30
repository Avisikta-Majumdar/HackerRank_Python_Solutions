n , m = map(int , input("").split(" "))
n_list=list(map(int , input("").split(" ")))
Set_A=set(int(x) for x in input("").split(" "))
Set_B = set(int(x) for x in input("").split(" "))
result=0
for i in n_list:
    if i in Set_A:
        result+=1
    elif i in Set_B:
        result-=1
    elif i not in Set_B and i not in Set_A:
        pass
print(result)
