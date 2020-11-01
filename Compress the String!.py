from itertools import groupby as a
s=input("")
key=[k for k, g in a(s)]
word= [list(g) for k, g in a(s)]
for i in range(len(key)):
    print("({}, {})".format(len(word[i]),key[i]),end=" ")
