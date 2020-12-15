def print_rangoli(size):
    width= (size+(size-1)+2*(size-1))
    n=size
    for i in range(n):
        s=''
        ch=96+n
        mid= ((2*i+1)//2)
        for j in range(2*i+1):
            s+=chr(ch)
            if j<mid:
                ch-=1
            else:
                ch+=1

            if j<(2*i):
                s+='-'
            else:
                pass
        print(s.center(width,'-'))
    for i2 in range(1,n):
        s=''
        ch=96+n
        mid= ((1+2*(n-1-i2))//2)
        for j2  in range(1+2*(n-1-i2)):
            s+=chr(ch)
            if j2<mid:
                ch-=1
            else:
                ch+=1

            if j2<(2*(n-1-i2)):
                s+='-'
            else:
                pass

        print(s.center(width,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
