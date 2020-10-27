if __name__ == '__main__':
    lst = []
    N = int(input())
    for i in range(N):
        mn= list(input("").split(" "))
        
        if mn[0]=="insert":
            a , b = map(int , (mn[1],mn[2]))
            lst.insert(a,b)


            
        elif mn[0]=="print":
            print(lst)
        elif mn[0]=="remove":
                lst.remove(int(mn[1]))

        elif mn[0]=="append":
            lst.append(int(mn[1]))
        elif mn[0]=="sort":
            lst.sort()
        elif mn[0]=="pop":
            
            lst.pop()
        elif mn[0]=="reverse":
            lst.reverse()
            
            

                
