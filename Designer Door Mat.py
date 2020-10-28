n, k = map(int , input("").split(" "))
st ='.|.'
st1='-'
avg = int((n+1)/2)
for i in range(1,1+n):
    if avg==i:
        print("WELCOME".center(k,st1))
    elif i<avg:
        print((st*(2*i-1)).center(k,st1))
    elif avg<i:
        print((st*(2*(n-i)+1)).center(k,st1))
