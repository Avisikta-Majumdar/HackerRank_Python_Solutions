if __name__ == '__main__':
    fl =[]
    m=[]
    for _ in range(int(input())):#Taking inputs
        name = input()
        score = float(input())
        l= list()#This l list is used for making nested lists like -->[name , score]
        l.append(name)
        l.append( score)
        m.append(score)
        fl.append(l)
    m.sort()
    mk = min(m)
    i=0
    mk1= mk
    while mk1 == mk:#Finding The second lowest grade here the cond. is mk1==mk because bef we initilize the min value to mk1 and mk1 want to take second lowest value
        mk1= m[i]
        i+=1

    na = []
    for i in fl:
        if i[1] == mk1:
            na.append(i[0])
    na.sort()
    for j in na:
        print(j)
