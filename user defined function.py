#Function with no argument and no return value.

def  printline():
        print("*"*50)

printline()
print("Welcome To User Defined Function in Python.")
printline()

#Function with argument with no return value.

def  add(a,b):
        print("Addition: ",a+b)

printline()
add(10,20)
printline()

#Function with argument and with return value.

def  sub(a,b):
        return a-b

printline()
#ans=sub(10,20)
print("Subtraction: ",sub(10,20))
printline()

