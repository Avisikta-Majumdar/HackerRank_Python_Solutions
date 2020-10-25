test_case = int(input(""))
for o in range(test_case):
    try:
        a ,b = map(int ,input("").split(" "))
        print(int(a/b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e1:
        print("Error Code:",e1)
    
    
