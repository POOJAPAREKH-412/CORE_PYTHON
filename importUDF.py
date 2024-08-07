import udf

while True:
    print("*"*40)
    print("1. oddeven")
    print("2. maxoftwo")
    print("3. maxofthree")
    print("4. fibonacii")
    print("5. primenumber")
    print("6. exit")
    print("*"*40)
    
    choice=int(input("Enter Your Choice: "))

    if choice==1:
        a=int(input("Enter Value: "))
        udf.odd_even(a)
        print("*"*40)
    elif choice==2:
        a=int(input("Enter Value of A: "))
        b=int(input("Enter Value of B: "))
        udf.max_of_two(a,b)
        print("*"*40)
    elif choice==3:
        a=int(input("Enter Value of A: "))
        b=int(input("Enter Value of B: "))
        c=int(input("Enter Value of C: "))
        udf.max_of_three(a,b,c)
        print("*"*40)
    elif choice==4:
        n=int(input("Enter Value: "))
        udf.prime_number(n)
        print("*"*40)
    elif choice==5:
        n=int(input("Enter Value: "))
        udf.fibonacii(n)
        print("*"*40)
    elif choice==6:
        print("Exiting the Programme")
        break
    else:
        print("Invalid Choice. Please Try Again Later")
        print("*"*40)
            

