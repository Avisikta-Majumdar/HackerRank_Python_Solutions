string = input("")
lower = list()
lower1 =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

upper = list()
upper1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
odd = list()
even= list()
number =['1','2','3','4','5','6','7','8','9','0']
for i in string:
    if i in lower1:
        lower.append(i)
    elif i in upper1:
        upper.append(i)
    elif i in number:
        even.append(i) if (int(i)%2==0) else odd.append(i)
lower.sort()
upper.sort()
even.sort()
odd.sort()
final = lower + upper + odd+even
for i in final:
    print(i,end = '')
