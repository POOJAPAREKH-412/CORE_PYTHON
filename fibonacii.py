# 0 1 1 2 3 5 8
a,b=0,1
n=int(input("enter N: "))
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b
