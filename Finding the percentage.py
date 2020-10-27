if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        j = student_marks.get(i)
        if i==query_name:
            result = 0
            for k in j:
                result+= float(k)
            print("{:.2f}".format((result/len(j))))
            break
        else:
            continue
