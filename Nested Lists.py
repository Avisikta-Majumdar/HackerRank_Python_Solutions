if __name__ == '__main__':
    final_list =[]
    marks=[]
    for _ in range(int(input())):
        l= list()
        l.append(input())
        score = float(input())
        l.append(score)
        marks.append(score)
        final_list.append(l)
    marks.sort()
    min_value = marks[0]
    marks.remove(min_value)
    for i in marks:
        if i>min_value:
            Result_value = i
            break
    Result_names=[]
    for i in range(len(final_list)):
        if Result_value in final_list[i]:
            Result_names.append(final_list[i][0])
    Result_names.sort()
    for i in Result_names:
        print(i)
