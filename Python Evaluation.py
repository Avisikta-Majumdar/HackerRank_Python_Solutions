inp = input("")
m=0
for i in (inp):
    if i=='(':
        s = inp[(m+1):-1]
        print(eval(s))
        break
    else:
        m+=1
