for i in range(1,10):
    print("*"*i)

for i in range(1,10):
    print(" "*(9-i),"*"*i)

for i in range(1,10):
    print(" "*(9-i)," *"*i)

for i in range(9,0,-1):
    print(" "*(9-i)," *"*i)

#Pascal's Triangle
n=5
c=0
for i in range(n+1):
    c=0
    for k in range(n,i,-1):
        print(end='  ')
    for j in range(i+1):
        print(c,end=' ')
        c+=(i-j)/j
