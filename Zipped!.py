No_Of_Students , X = map(int,input("").split(" "))
final_list=[]
for i in range(X):
    lst = [float(x) for x in input("").split(" ")]
    final_list.append(lst)
for i in zip(*final_list):
    print((sum(i)/len(i)))


