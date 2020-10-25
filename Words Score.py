def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(arr):
    final=0
    for word in arr:
        s=0
        result =0#if s is odd then add 1 otherwise add 2
        for i in word:
            if is_vowel(i):
                s+=1
            else:
                pass
        if s&1==1:
            result+=1
        else:
            result+=2
        final+=result
    return final

n = int(input())
words = input().split()
print(score_words(words))
