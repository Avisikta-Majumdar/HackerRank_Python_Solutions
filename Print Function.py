if __name__ == '__main__':
    n = int(input())
    x = 1
    c = ""
    for x in range(n):
        x = x + 1
        a = int(n) - int(x)
        b = int(n) - int(a)
        c = str(c) + str(b)

    print(c)