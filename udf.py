def odd_even(n):
    if n%2==0:
        print("This Number is Even.")
    else:
        print("This Number is Odd.")

def max_of_two(a,b):
    if a>b:
        print(a," A is max number")
    else:
        print(b," B is min number")

def max_of_three(a,b,c):
    if a>b:
        if a>c:
            print("A is max")
        else:
            print("C is max")
    elif b>c:
        print("B is max")
    else:
        print("C is max")

def prime_number(n):
    if n%2!=0:
        for i in range (3,int(n/2)+1,2):
            if n%i==0:
                print(n," is not prime ")
                break
        else:
            print(n," is prime ")

    else:
        print(n," is not prime ")

def  fibonacii(n):
        a,b=0,1
        print(a,end=" ")
        while b<n:
            print(b,end=" ")
            a,b=b,a+b
            
        
    


    
