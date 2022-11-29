# # 2. Write a program to input item details: name, price, quantity, code. Then compute the invoice item wise 
# # and total bill. Display the result in proper format.


class item:
    def __init__(self) -> None:
        self.name=""
        self.price=0
        self.quantity=0
        self.code=""
    
    def input(self):
        self.name=input("Name of item : ")
        self.price=int(input("Prize per item : "))
        self.quantity=int(input("Quantity : "))
        self.code=input("Code : ")
    
class invoice(item):
    def compute(self):
        print("-"*31)
        print("Name : ",self.name)
        print("Code : ",self.code)
        print("Quantity : ",self.quantity)
        print("Prize per item : ",self.price)
        print("Total prize : ",self.price*self.quantity)
        print("-"*31)


ob=invoice()
ob.input()
ob.compute()

