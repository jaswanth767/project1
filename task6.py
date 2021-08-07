import operator
teststr = 'mississippi'
strdict = dict()
for letter in teststr:
    if letter not in strdict:
        strdict[letter]=teststr.count(letter)
answer = sorted(strdict.items(),key = operator.itemgetter(1),reverse=True)
for i in range(len(answer)):
    print(answer[i])
