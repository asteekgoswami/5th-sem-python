# 1. Write a program to create a class BankAccount, which contains the data members account_number, customer_name, account_type, balance and class methods deposit(), withdraw(), and summary().
# Include an option that a user can withdraw a maximum amount of rupees 10000/- per transaction and the balance must meet the minimum balance amount of rupees 1000/- in the account


class BankAccount:
    def __init__(self) -> None:
        self.account_number=0
        self.customer_name=''
        self.account_type=''
        self.balance=0

    def deposite(self):
        amount=int(input("Enter the amount : "))
        self.balance=int(self.balance)+amount
        print("Deposite successfully !")

    def withdraw(self):
        amount=int(input("Enter the amount : "))
        if amount>10000:
            print("Exceed the limit of maximum amount per transaction")
        else:
            if self.balance-amount<1000:
                print("Not able to Withdraw because Minimun balance become less than 1000")
            else:
                self.balance=self.balance-amount
                print("Withdraw successfully !")

    def summary(self):
        print("-"*30)
        print("Account Number : ",self.account_number)
        print("Customer Name : ",self.customer_name)
        print("Account Type : ",self.account_type)
        print("Balance : ",self.balance)
        print("-"*30)

    def getdata(self):
        self.account_number=input("Account Number : ")
        self.customer_name=input("Customer Name : ")
        self.account_type=input("Account Type : ")
        self.balance=input("Balance : ")


ob=BankAccount()
ob.getdata()
while True:
    print("*"*30)
    print("Press 1 for Deposite : ")
    print("Press 2 for Withdraw : ")
    print("Press 3 for Summary : ")
    print("Press any other to exit : ")
    print("*"*30)
    op=input("Enter option : ")
    
    match op :
        case '1':
            ob.deposite()
        case '2':
            ob.withdraw()
        case '3':
            ob.summary()
        case _:
            exit()


