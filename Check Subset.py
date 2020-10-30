def Subset(a,b):
    result = 0
    for i in a:
        if i in b:
            result = 1
        else:
            result = 0
            break
    return True if result == 1 else False# Using Ternary Operator

test_case = int(input(""))
for i in range(test_case):
    a= int(input(""))
    seta = set(int(x) for x in input().split(" "))
    b =int(input(""))
    setb = set(int(x) for x in input().split(" "))
    print(Subset(seta , setb))
