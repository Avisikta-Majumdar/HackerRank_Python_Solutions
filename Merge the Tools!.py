def merge_the_tools(string, k):
    for i in range(len(string)//k):
        s=string[k*i:k*i+k]
        l=[i for i in s]
        a=''
        for i in l:
            if i not in a:
                a+= i
        print(a)
    #    print(s)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
