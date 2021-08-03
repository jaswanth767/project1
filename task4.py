def feb(n):
    if n<=0:
        print("Invalid number")
    elif n==1:
        print(0)
    else:
        i = 0
        j = 1
        print(i,end=" ")
        print(j,end=" ")
        for h in range(n-2):
            k = i+j
            i=j
            j=k
            print(k,end=" ")
x = int(input("enter no of steps :"))
feb(x)
