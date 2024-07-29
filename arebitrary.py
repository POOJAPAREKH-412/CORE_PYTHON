def  test(a,b,c,*d,**e):
        print("A: ",a," B: ",b," C: ",c," D: ",d," E: ",e)

test(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)


def  test(a,b,c,*d,**e):
        print("A: ",a," B: ",b," C: ",c," D: ",list(d)," E: ",e)

test(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)


def  test(a=10,b=20,c=30,*d,**e):
        print("A: ",a," B: ",b," C: ",c," D: ",d," E: ",e)

test(10,20,30,40,50,d=60,e=70)
