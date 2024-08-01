class Bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("Hello ",cname," , Your Account Number is: ",acno,"and  Your Bank Balance is: ",balance)

    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance")

    def checkBalance(self):
        print("Current Balance",self.balance)
        print("*"*40)
          
b1=Bank( )
b1.openAccount(101,"Shruti",1000)

while True:
    print("*"*40)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*40)

    Choice=int(input("Enter Your Choice: "))
    
    if Choice==1:
         amount=int(input("Enter Deposit Amount: "))
         b1.deposit(amount)
         print("*"*40)
    elif Choice==2:
        amount=int(input("Enter Withdraw Amount: "))
        b1.withdraw(amount)
        print("*"*40)
    elif Choice==3:
         b1.checkBalance()
         print("*"*40)
    elif Choice==4:
        print("Thank You For Using Our Services.")
        print("*"*40)
        break
    else:
        print("Invalid Choice. Please Try Again")
        print("*"*40)
                
        
