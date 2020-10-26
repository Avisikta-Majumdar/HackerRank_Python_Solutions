###1st Condition - All number must be Positive 
###2nd Condition - Atleast one number must be Palidrome
N =int(input(""))
n = list(map(int , input("").split(" ")))
if (all(i>0 for i in n) and any(str(i)==str(i)[::-1] for i in n)):#if all the numbers is positive then it will return True    
    print(bool(1))
else:
    print(bool(0))
