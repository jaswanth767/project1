lst =[]
n = int(input("enter no of elements u enter in a list  : "))
for i in range(n):
    x = int(input("enter the number :"))
    lst.append(x)
print("Input :",lst)
nums = list(filter(lambda f:f>0,lst))
print("Output :",nums)
