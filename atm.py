print("WELCOME TO VISAKA BANK!!!")
cardNumber=input("Please kindly enter your card number:  ")
cardPass=input("Please enter the password:  ")
balance=int(input("Balance Amount:  "))

class atm():
    def __init__(self,balace):
        self.balance=balance
    
    def withdrawl(self,withDrawAmount):
        self.balance=self.balance-withDrawAmount
        print(self.balance)

    def increase(self,increase):
        self.balance=self.balance+increase
        print(self.balance)

    def showBalance(self):
        print(self.balance)

atm1=atm(balance)
while(1):
    print("What Do You Look For: 1.Balance \n                      2.Withdrawal \n                      3.Increase the Amount")
    task=input("Which one do you choose: ")
    if(task=="balance"):
        atm1.showBalance()
    elif(task=="withdrawal"):
        x=int(input("Enter the withdrawal amount: "))
        atm1.withdrawl(x)
    elif(task=="increase the amount"):
        y=int(input("Enter the increased amount: ")) 
        atm1.increase(y)  
    else:
        print("Please follow the instructions") 
    