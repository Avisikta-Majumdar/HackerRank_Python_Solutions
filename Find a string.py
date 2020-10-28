def count_substring(string, sub_string):
    len_SubString= len(sub_string)
    result = 0
    for i in range(len(string)+1-len_SubString):
        if string[i:i+len_SubString]==sub_string:
            result+=1
        else:
            continue
    
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
