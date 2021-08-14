def count(string):
    h = []
    g = []
    for j in string:
        t = j
        x=0
        for i in string:
            if i == t:
                x+=1
        h.append(t)
        g.append(x)
    f = dict(zip(h,g))
    sorted_form = sorted(f.items(),key = lambda kv: kv[1])
    for i in sorted_form:
        print(i)
str_input = input("Enter the string :")
count(str_input)
