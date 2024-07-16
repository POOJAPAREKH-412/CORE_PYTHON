a=int(input("enter value of A: "))
b=int(input("enter value of B: "))
c=int(input("enter value of C: "))

if a>b:
    if a>c:
        print("A is max")
    else:
        print("C is max")
elif b>c:
    print("B is max")
else:
    print("C is max")
    

