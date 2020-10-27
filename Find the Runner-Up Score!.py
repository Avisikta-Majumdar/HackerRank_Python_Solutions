if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max1=arr[-1]
    arr.sort(reverse=True)
    for x in arr:
        if x!=max1:
            result = x
            print(result)
            break
    
